import os
import sys

from cleo import Command

class InitTemplateCommand(Command):
    """
    Init new config file base-ed on template. Supported project type: php, ruby, android

    init
        {project_type : This will overwrite any existing config file}
    """

    def handle(self):
        project_type = self.argument('project_type')
        if project_type not in self.app.PROJ_TYPES:
            self.line('<error>Invalid project type !</error>')
        else:
            file_path = os.path.join(self.app.TEMPLATES_DIR, "%s.yml" % project_type)
            with open(file_path, "r") as fin:
                with open(self.app.configure_file_name, "w") as fout:
                    fout.write(fin.read())
                    self.line('<info>Wrote to file: %s</info>' % self.app.configure_file_name)
        sys.exit(0)
