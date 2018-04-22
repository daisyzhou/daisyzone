from collections import namedtuple

# [start, end)
ModificationRange = namedtuple("ModificationRange", ["start", "end"])
TemplateModification = namedtuple("TemplateModification", ["mod_range", "description"])


class Template(object):
    """
    An immutable MadLibs template.
    """
    def __init__(self, original_text, template_modifications):
        """

        :param original_text:
        :param template_modifications: List of TemplateModification.  No modification may overlap.
        """
        self._original_text = original_text
        # Validate no overlapping ranges
        sorted_template_modifications = sorted(template_modifications, key=lambda t_m: t_m.mod_range.start)
        self._validate_modification_ranges(sorted_template_modifications)
        self._modifications = sorted_template_modifications

    def _validate_modification_ranges(self, sorted_template_modifications):
        prev_end = 0
        for modification in sorted_template_modifications:
            mod_range = modification.mod_range
            if mod_range.end <= mod_range.start:
                raise ValueError("End of range must be after start.")
            if mod_range.start < 0:
                raise ValueError("Cannot modify negative index")
            if mod_range.start < prev_end:
                raise ValueError("Overlapping modifications not allowed in template_modifications.")
            if mod_range.end > len(self._original_text):
                raise ValueError("Modification range longer than length of original text.")
            prev_end = mod_range.end

    def fill_in_answers(self, answers):
        """

        :param answers: List of strings to fill in
        :return: String with answers filled in
        """
        if len(answers) != len(self._modifications):
            raise ValueError("Wrong number of answers: expected {}, got {}".format(len(self._modifications), len(answers)))

        # Build up result by adding the in between chunks
        result_so_far = ""
        prev_end = 0
        for (answer, modification) in zip(answers, self._modifications):
            result_so_far = result_so_far + self._original_text[prev_end:modification.mod_range.start] + answer
            prev_end = modification.mod_range.end
        result_so_far += self._original_text[prev_end:]
        return result_so_far

    def get_modifications(self):
        return self._modifications


def test():
    test_template = Template("hay is for horses, don't you know", [TemplateModification(ModificationRange(0, 3), "noun"), TemplateModification(ModificationRange(11, 17), "noun2")])
    print(test_template.fill_in_answers(["poop", "otherpoop"]))

    test_template2 = Template("hay is for horses, don't you know", [TemplateModification(ModificationRange(4, 6), "is"), TemplateModification(ModificationRange(29, 33), "verb")])
    print(test_template2.fill_in_answers(["isn't", "poop"]))
