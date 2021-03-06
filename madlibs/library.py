from random import shuffle

from madlibs.template import Template, TemplateModification, ModificationRange


library = {
   "hay": Template(
       "hay is for horses, don't you know",
       [
           TemplateModification(ModificationRange(0, 3), "noun"),
           TemplateModification(ModificationRange(11, 17), "plural noun")
       ]),

   "teamcomp": Template(
        "In any team you need a tank, a healer, a damage dealer, someone with crowd control abilities, and another who knows iptables.",
        [
            TemplateModification(ModificationRange(23, 27), "profession"),
            TemplateModification(ModificationRange(31, 37), "profession"),
            TemplateModification(ModificationRange(41, 47), "noun"),
            TemplateModification(ModificationRange(69, 82), "noun"),
            TemplateModification(ModificationRange(116, 124), "noun"),
        ]
    )
}


def get_random_name():
    return get_names()[0]


def get_names():
    keys = list(library.keys())
    shuffle(keys)
    return keys


def get_by_name(name):
    return library[name]


def add_template(name, template):
    if name in library:
        raise ValueError("Name {} already taken".format(name))
    library[name] = template
