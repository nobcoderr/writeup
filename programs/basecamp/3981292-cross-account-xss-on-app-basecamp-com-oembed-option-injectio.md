# Cross-account XSS on app.basecamp.com: oEmbed option injection chained through Turbo defeats the CSP nonce

- Program: Basecamp
- Weakness / temuan: **Cross-site Scripting (XSS) - Generic**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 27
- Submitted: 2026-08-30
- Disclosed: 2026-10-28
- Report: https://hackerone.com/reports/3981292

## Team summary

**Summary**

Basecamp's embed display page renders the HTML an embed provider returns. It needs no sign-in, and because it renders that HTML as is, it should answer only on a separate, cookieless embeds host. Its host check compared the request's registrable domain (basecamp.com) with the application's full host name (3.basecamp.com, or app.basecamp.com once we added that name). Those could never be equal, so the check never blocked a request on either application host, before or after the move to app.basecamp.com. Our earlier summary blamed that domain migration; that was wrong.

The attack also needed markup an attacker could shape. deivizzzz supplied it through one provider's oEmbed response, which copied options from the pasted URL into its embed code.

**Impact**

An attacker with their own Basecamp account could create such an embed and send a link. A signed-in user in another account who opened it ran the attacker's script on app.basecamp.com, in their own session. In the researcher's demonstration, the script read the victim's CSRF token and private profile and wrote to the profile as the victim.

We rated it High, CVSS 8.7 (CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:N), with Privileges Required Low because the attack needs an account of the attacker's own to create the embed.

**Fix**

The check now fails closed: the page renders only for the embeds host. That was live on our main production servers at 04:51 UTC on 31 August 2026, under seven hours after the report, and on a smaller pool of production servers that serves some accounts at 17:48 UTC on 1 September. A browser that opens the page on app.basecamp.com or 3.basecamp.com now gets a 403.

Separately, that provider's embeds, stored ones included, now render as at most a player frame built from the media's id, so options in a pasted URL no longer reach the embed HTML.

**Timeline**

- 2026-08-30 22:00 UTC: Report submitted
- 2026-08-31 04:51 UTC: Fix live on the main production servers
- 2026-08-31 05:15 UTC: Triaged and resolved
- 2026-09-01 17:48 UTC: Fix live on the smaller pool
- 2026-10-27: Provider embed change deployed
- 2026-10-28: Limited disclosure

Thanks to deivizzzz for a thorough, well-documented report.
