import base64
import logging
import urllib.parse
from datetime import datetime
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from flask import Blueprint, redirect, request, session
from flask.globals import current_app

from bdauth.auth import login_required

logging.basicConfig(level=logging.INFO)


bp = Blueprint('openurl', __name__, url_prefix='/openurl')


@bp.route("/")
@login_required
def construct_url():
    bdurl = current_app.config['BD_URL']

    code = 307
    url = bdurl + pi_encryptor() + "&query=" + query_formatter(request.args)
    return redirect(url, code)


def pi_encryptor():
    if current_app.config['ENV'] == 'testing':
        return '&PI=' + session['samlKerbid']

    decoded_key = base64.standard_b64decode(current_app.config['BD_KEY'])
    pubkey = RSA.importKey(decoded_key)
    logging.info(f"pubkey: {pubkey}")

    now = datetime.utcnow().strftime("%Y%m%d %H%M%S")
    plaintext = f"{session['samlKerbid']}|{now}"
    logging.info(f"plaintext: {plaintext}")

    cipher = Cipher_PKCS1_v1_5.new(pubkey)
    e = cipher.encrypt(plaintext.encode('utf-8'))
    logging.info(f"encrypted: {e}")

    return '&PI=' + base64.urlsafe_b64encode(e).decode('utf-8')


def query_formatter(args):
    bdquery = ""
    joiner = ""

    # current prod logic seems to be:
    # if isbn
    #   use isbn and nothing else
    # else if any of the 4 titles exist:
    #   use the title that exits in this preferential order
    #      title, btitle, ctitle, jtitle
    #      nested condition of if aulast include that as well

    isbn = args.get('rft.isbn')
    if isbn:
        bdquery += "isbn=\"" + isbn + "\""
        return urllib.parse.quote(bdquery)

    aulast = args.get('rft.aulast')

    title = args.get('rft.title')
    if title:
        bdquery += "ti=\"" + title + "\""
        joiner = " and "
        if aulast:
            bdquery += joiner + "au=\"" + aulast + "\""

        return urllib.parse.quote(bdquery)

    title = args.get('rft.btitle')
    if title:
        bdquery += "ti=\"" + title + "\""
        joiner = " and "
        if aulast:
            bdquery += joiner + "au=\"" + aulast + "\""

        return urllib.parse.quote(bdquery)

    title = args.get('rft.ctitle')
    if title:
        bdquery += "ti=\"" + title + "\""
        joiner = " and "
        if aulast:
            bdquery += joiner + "au=\"" + aulast + "\""

        return urllib.parse.quote(bdquery)

    title = args.get('rft.jtitle')
    if title:
        bdquery += "ti=\"" + title + "\""
        joiner = " and "
        if aulast:
            bdquery += joiner + "au=\"" + aulast + "\""

        return urllib.parse.quote(bdquery)

    # if nothing matches, just return. no search will be done
    return ''
