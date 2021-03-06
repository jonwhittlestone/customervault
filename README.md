# customervault

![CI](https://github.com/jonwhittlestone/customervault/workflows/CI/badge.svg)

![Deploy to Production](https://github.com/jonwhittlestone/customervault/workflows/Deploy%20to%20Production/badge.svg)

customervault.app gives your customers the ability to simply store and retrieve the assets you've produced.

For individual stack details see:

- [`api/README.md`](https://github.com/jonwhittlestone/customervault/tree/main/api)
- [`front/README.md`](https://github.com/jonwhittlestone/customervault/tree/main/front)

CI and Deploy to PaaS with Github Actions.

## CI

A push or pull request to main will trigger running [API tests](https://github.com/jonwhittlestone/customervault/blob/main/.github/workflows/main.yml) and [frontend build and tests](https://github.com/jonwhittlestone/customervault/blob/main/.github/workflows/ci_front.yml)

## Deploy

A push to [release branch](https://github.com/jonwhittlestone/customervault/tree/release) will trigger a [deploy API to PaaS and deploy to frontend](https://github.com/jonwhittlestone/customervault/blob/main/.github/workflows/deploy.yml) the static file hosting.

To get github-pages functioning nicely with DNS:

1. Set your repo settings
   ![](docs/screenshots/gh-pages.png)

2. Set your DNS CNAME and A record
   ![](docs/screenshots/dns.png)

3. Set a GitHub verified domain
   - https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages

## License

This project is licensed under the terms of the MIT license.
