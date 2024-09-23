import docutils.nodes as nodes
import sphinx.addnodes as addnodes

TEMPLATE_COMPONENTS = {
    addnodes.document: ("document", "Document"),
    nodes.paragraph: ("paragraph", "Paragraph"),
    nodes.raw: ("raw", "Raw"),
    nodes.literal_block: ("code_block", "CodeBlock"),
    nodes.strong: ("strong", "Strong"),
    nodes.bullet_list: ("bullet_list", "BulletList"),
    nodes.list_item: ("list_item", "ListItem"),
    nodes.substitution_definition: ("no_output", "NoOutput"),
    nodes.title: ("title", "Title"),
}
