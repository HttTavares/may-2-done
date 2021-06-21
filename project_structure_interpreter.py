from db import project_data_base

class ProjectInterpreter():
    def __init__(self, project_data):
        self.project_data = project_data

    def get_project_by_id(self, project_id):
        pass

    def get_structure_text_byid(self, project_id):
        pass

    def line_breaker(self, project_structure_text):
        return project_structure_text.split('\n')

    def hashtag_counter(self, text_line):
        return len(text_line) - len(text_line.replace('#', ''))

    def find_step_lines(self, splitted_project):
        step_lines = []
        for line_index in range(len(splitted_project)):
            if self.hashtag_counter(splitted_project[line_index]) == 1:
                step_lines.append(line_index)
        return step_lines

    def split_into_steps(self, splitted_project):
        i = 0
        step_lines = self.find_step_lines( splitted_project )
        # if len(splitted_project) == 0:
        #     pass
        # while i < len(step_lines):
        #     if i == len(step_lines):
        #         pass


    def project_interpreter_test(self):
        project_text = self.project_data['maydo'][0]['structure text']
        splitted = self.line_breaker(project_text)
        project_structure = {'steps': {}}

        # for thing in self.split_into_steps( splitted ):
        #     print(splitted[thing])
        # for line in splitted:
        #     if self.hashtag_counter(line) == 1:
                # project_structure['steps'][line.replace('#', '')] = {'substeps':{}}

            # print(self.hashtag_counter(line))
            # project_structure[self.hashtag_counter(line)]
