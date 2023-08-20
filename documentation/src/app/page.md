---
title: Welcome to the django realms documentation.
---

Kickstarting your Big SaaS idea using a django grapqhl and react techstack has never been easier thanks too [DjangoRealms](https://realms.imperisoft.co.uk) {% .lead %}

{% quick-links %}

{% quick-link title="Getting Started" icon="architecture" href="/deployment" description="The guide for how we deploy VastDesk to both staging and production." /%}

{% quick-link title="Code Architecture" icon="architecture" href="/architecture" description="The guide for how we structure our code and directrory structure." /%}

{% quick-link title="Git Guide" icon="github" href="/git-guide" description="Our Git guide explaining how we use it for a smooth development process." /%}

{% quick-link title="Writing Documentation" icon="pencil" href="/writing-documentation" description="Learn to how to write and create beatiful and informative documentation." /%}

{% /quick-links %}

---

## Getting Started

To contribute to VastDesk, the first thing you need to do is fork the repository which you will find [here](https://github.com/vastdesk/vastdesk). Once on that page you will find the fork button in the top right corner. Once you have forked the repository, you will need to clone it to your local machine. To do this, you will need to run the following command in your terminal:

```shell
git clone git@github.com:YOUR_USERNAME/vastdesk.git
```

Once you have cloned the repository, you will need to ensure you have the upstream set up correctly. To do this, you will need to run the following command in your terminal:

```shell
git remote -v
```

You should see something like this:

```shell
origin  https://github.com/YOUR_USERNAME/vastdesk (fetch)
origin  https://github.com/YOUR_USERNAME/vastdesk (push)
upstream        https://github.com/VastDesk/vastdesk.git (fetch)
upstream        https://github.com/VastDesk/vastdesk.git (push)
```

If your upstream is not set to the VastDesk repository, you will need to run the following command in your terminal:

```shell
git remote add upstream git@github.com:vastdesk/vastdesk.git
```

### Installing dependencies

The next step is to start installing all the dependencies. To do this, you will need to run the following command in your terminal:

```shell
tools/prep-dev-environment
```

You will also need to ensure you have Docker Desktop installed as well as WSL installed if working on Windows. You can find the Docker Desktop installation instructions [here](https://docs.docker.com/get-docker/). You can find the WSL installation instructions [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10). On Linux, you will need to ensure you have Docker installed. You can find the Docker installation instructions [here](https://docs.docker.com/engine/install/).
