# bd_auth

## Local development

- `python3-saml` package requires `libxmlsec1`.
  Suggest `brew install libxmlsec1` on macOS
- possibly also needs `pkg-config` (not sure)
- authentication is bypassed in development and testing environments. set `FAKE_USER` to what you want to simulate.

## Required ENV in production

`BD_KEY` = the supplied public key, base64encoded, for borrowdirect

`BD_URL` = the borrowdirect URL

`FLASK_APP` = bdauth

`FLASK_ENV` = production

`IDP_CERT` = standard IST IDP setting

`IDP_ENTITY_ID` = standard IST IDP setting

`IDP_SSO_URL` = standard IST IDP setting

`SECRET_KEY` = generate a long random string. Used for session security

`SP_ACS_URL` = route in this app that handles the response from IDP

`SP_CERT` = obtained from self signed cert generated for this app

`SP_ENTITY_ID` = domain name of app + /saml

`SP_KEY` = obtained from self signed key generated for this app

`URN_UID` = the key in the SAML response to pull the kerberos ID

## Required ENV

`SENTRY_DSN` = if set to a valid Sentry DSN, enables Sentry exception monitoring
