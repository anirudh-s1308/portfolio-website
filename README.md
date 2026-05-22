portfolio/
├── app/
│   ├── data/
│   │   └── projects.py          # Add new projects here only
│   ├── routes/
│   │   ├── home.py
│   │   └── projects.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── img/
│   ├── templates/
│   │   ├── base.html            # nav, footer, shared layout
│   │   ├── home.html            # extends base, shows featured projects
│   │   └── projects.html        # extends base, shows all projects
│   └── main.py                  # app init, mounts static, includes routers
