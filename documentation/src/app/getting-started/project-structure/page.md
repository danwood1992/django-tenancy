---
title: Project Structure
---

Structure in any project is paramount {% .lead %}

{% quick-links %}

{% quick-link title="Frontend" icon="clipboard-document-list" href="/project-structure/frontend" description="Dive deep into the Frontend structure powered by NextJs and React." /%}

{% quick-link title="Backend" icon="folder" href="/project-structure/backend" description="Explore the Backend realm driven by Django and Graphene." /%}

{% /quick-links %}

## Overview 

This page provides an overview of Django Realms' project and directory structure as a whole. To delve deeper into specific sections, follow the backend or frontend links above.
## Top Level Directory

The top-level file and folder structure of Django Realms is as follows, follow the links to go deeper:

#### dot files

🔒 [.env]                   - Environment variables for the project.  
🌐 .git                  - Git source directory.  
📝 .gitattributes        - Attributes for pathnames to be used by git.  
🛠  .gitignore            - Specifies intentionally untracked files  

#### markdown files
📖 CONTRIBUTING.md       - Guidelines for contributing to the project.  
📜 LICENSE.md            - Project license details.  
📚 README.md             - Introductory documentation.  

#### Directories
📦 [apps](/tree/apps)    - All the application modules and components.    
📘 documentation         - This documentation site.   
🚢 [compose](/tree/compose) - Contains Docker-related files for setting up containers.    
🌐 [django_realms](project-structure/tree/django_realms) - Core project directory.   
🎨 [django_realms-frontend](/tree/django_realms-frontend) - Frontend files and components.  
🗒  logs                 - Directory containing logs. 

#### Script Files
📄 [docker-compose-prod.yml](/tree/compose-prod)  - Docker Compose configuration for production.  
📄 [docker-compose.yml](/tree/compose)    - Docker Compose configuration for development.  
🚀 manage.py             - Utility script to manage Django tasks. 
📄 requirements.txt      - Lists all Python dependencies for the project.

#### Environemnt Files
📦 venv                 - Python virtual environment for the project.

## TechStack

What Ties it all together? {% .lead %}

### Starting with the Frontend



#### NextJs

##### For our frontend, we've chosen the NextJs Framework, a decision rooted in our admiration for its capabilities and the dynamism it brings.

NextJs serves as a powerful framework for building React applications, bolstered by both server and client-side rendering capabilities. Its popularity and large community support played a pivotal role in our choice. For the project's frontend structure, we've predominantly adhered to the [Next Js conventions](https://nextjs.org/docs). 


### Django and Graphene

On the backend, we lean on the robustness of Django coupled with the versatility of Graphene. Django a high-level Python Web framework, serves as the backbone of our backend. And Graphene, a Python library for building GraphQL APIs, is the driving force behind our backend's API layer.








