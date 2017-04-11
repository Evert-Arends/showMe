from showMe.controllers.models import logs

fine = logs.query.all()
for item in fine:
    print [item.name, item.icon, item.path]
