# 2. Use SAML SP

Date: 2021-06-10

## Status

Accepted

## Context

BorrowDirect requires a solution that works with our Touchstone system. They do
not provide SAML support on the BorrowDirect side like most vendors would.

Historically, we have used `mod_shib` and a custom script to authorize the user
and send through the information necessary to BorrowDirect.

The server that runs that script is going away during the migration.

Using a SAML SP instead of `mod_shib` allows us to use Cloud infrastructure
instead of dedicated VMs to support this service.

Some institutions use EZproxy to authenticate, but our setup does not align with
how they have done things in a way that for us to do the same we'd need to
remove some elements that increase the privacy / security involved in the
system. Details in: https://mitlibraries.atlassian.net/browse/IMP-2104

## Decision

We will use a SAML SP

## Consequences

Using a SAML SP will allow us to use our typical Cloud solutions, such as
Heroku, to get stage/prod environments, CI/CD Pipelines, centralized logging,
and error reporting.
