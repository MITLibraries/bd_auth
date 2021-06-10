# 3. Use Python and Flask

Date: 2021-06-10

## Status

Accepted

## Context

We need to build a solution that can be build rapidly, be maintained by our
existing staff, and can integrate with IST Touchstone while also being able to
be deployed in our typical Cloud infrastructure solutions and can readily solve
the needs of the application (namely encrypting some values and contructing
specific URL parameters).

## Decision

We will use Python and the Flask framework.

## Consequences

We have more Python support across teams than other languages so choosing a
language with more support should allow for transitioning to ITS.

We can leverage specific production applications that have been running for long
periods of time with SAML SPs integrated with Touchstone using Flask on Heroku.
