# .tooltip - dropdown - content.red
# {
#     border: 1px solid red;
# }

#         /* RED */
#         .row.red {
#             background-color: #a75d5d;
#             border-bottom: 1px solid red;
#             border-top: 1px solid red;
#         }
#
#         .row.red:hover {
#             background-color: #c24646;
#             border: 1px solid red;
#         }
#
#         .box.red {
#             background-color: #c42020;
#             border: 1px solid red;
#         }
#
#         .row.red:hover > .number {
#             font-weight: bold;
#         }


class ColorDef:
    def __init__(self, background, border):
        self.background = background
        self.border = border


class ColorHoverDef:
    def __init__(self, background_from, background_to):
        self.background_from = background_from
        self.background_to = background_to


class ColorSet:
    def __init__(self, name, static, hover, box, tooltip=None):
        self.name = name
        self.static = static
        self.hover = hover
        self.box = box
        self.tooltip = tooltip

    def __str__(self):
        return f"""
            /* --------------------- {self.name} --------------------- */
            .row.{self.name} {{
                background-color: {self.static.background};
                border-bottom: 1px solid {self.static.border};
                border-top: 1px solid {self.static.border};
            }}

            .text-{self.name} {{
                color: {self.static.border}
            }}

            /*.row.{self.name}:hover {{
                background-color: ;
            }}*/

            .box.{self.name} {{
                background-color: {self.box.background};
                border: 1px solid {self.box.border};
            }}

            .row.{self.name}:hover > .number {{
                font-weight: bold;
            }}
            
            .row.{self.name}:hover {{
                animation: {self.name}-hover-animation 1s infinite;
            }}

            /*
            @keyframes {self.name}-hover-animation {{
                from {{background-color: {self.hover.background_from};}}
                to {{background-color: {self.hover.background_to};}}
            }}*/
            
            .tooltip-dropdown-content.{self.name}
            {{
                border: 1px solid {self.box.border};
            }}
        """


colors = []

colors.append(ColorSet("exp-red", ColorDef("#a75d5d", "red"), ColorHoverDef("#c24646", "red"), ColorDef("#c42020", "red")))

colors.append(ColorSet("red", ColorDef("#8c0000", "#ff0000"), ColorHoverDef("#4d0000", "#b70000"), ColorDef("#8c0000", "#ff0000")))
colors.append(ColorSet("dark-red", ColorDef("#200000", "#ff0000"), ColorHoverDef("#4d0000", "#b70000"), ColorDef("#200000", "#ff0000")))

colors.append(ColorSet("green", ColorDef("#008c00", "#00ff00"), ColorHoverDef("#00a900", "#007200"), ColorDef("#008c00", "#00ff00")))
colors.append(ColorSet("dark-green", ColorDef("#002000", "#00ff00"), ColorHoverDef("#00a900", "#007200"), ColorDef("#008c00", "#00ff00")))
# colors.append(ColorSet("dark-green2", ColorDef("#1b4d1b", "#006700"), ColorHoverDef("#1b4d1b", "#006700"), ColorDef("#1b4d1b", "#006700")))

colors.append(ColorSet("blue", ColorDef("#00009f", "#0000ff"), ColorHoverDef("#00005d", "#0000b9"), ColorDef("#0000bf", "#0000ff")))
colors.append(ColorSet("dark-blue", ColorDef("#000020", "#0000ff"), ColorHoverDef("#00005d", "#0000b9"), ColorDef("#0000bf", "#0000ff")))

colors.append(ColorSet("yellow", ColorDef("#8c8c00", "#ffff00"), ColorHoverDef("#545400", "#b2b200"), ColorDef("#8c8c00", "#ffff00")))
colors.append(ColorSet("dark-yellow", ColorDef("#202000", "#ffff00"), ColorHoverDef("#545400", "#b2b200"), ColorDef("#8c8c00", "#ffff00")))

colors.append(ColorSet("gray", ColorDef("#272727", "#5e5e5e"), ColorHoverDef("#272727", "#525252"), ColorDef("#272727", "#525252")))
colors.append(ColorSet("dark-gray", ColorDef("#151515", "#5e5e5e"), ColorHoverDef("#272727", "#444444"), ColorDef("#151515", "#424242")))

colors.append(ColorSet("violet", ColorDef("#830083", "#ff00ff"), ColorHoverDef("#8c008c", "#935193"), ColorDef("#8c008c", "#ff00ff")))
colors.append(ColorSet("dark-violet", ColorDef("#200020", "#ff00ff"), ColorHoverDef("#200020", "#935193"), ColorDef("#200020", "#ff00ff")))

colors.append(ColorSet("orange", ColorDef("#cb7b00", "#ffcb16"), ColorHoverDef("#965d00", "#d28800"), ColorDef("#cb7b00", "#ffcb16")))
colors.append(ColorSet("dark-orange", ColorDef("#200f00", "#ffcb16"), ColorHoverDef("#200f00", "#d28800"), ColorDef("#200f00", "#ffcb16")))

colors.append(ColorSet("pink", ColorDef("#c63e7d", "#ff81cf"), ColorHoverDef("#c63e7d", "#b75c88"), ColorDef("#c63e7d", "#ff81cf")))
colors.append(ColorSet("dark-pink", ColorDef("#200d10", "#ff81cf"), ColorHoverDef("#200d10", "#b75c88"), ColorDef("#200d10", "#ff81cf")))

colors.append(ColorSet("cyan", ColorDef("#00b1b4", "#31fffc"), ColorHoverDef("#00b1b4", "#007373"), ColorDef("#00b1b4", "#31fffc")))
colors.append(ColorSet("dark-cyan", ColorDef("#001f20", "#31fffc"), ColorHoverDef("#001f20", "#007373"), ColorDef("#001f20", "#31fffc")))

colors.append(ColorSet("navy", ColorDef("#242f60", "#394eba"), ColorHoverDef("#0f1020", "#5959c9"), ColorDef("#2f3f7f", "#394eba")))
colors.append(ColorSet("dark-navy", ColorDef("#0f1020", "#394eba"), ColorHoverDef("#0f1020", "#3a3aa1"), ColorDef("#0f1020", "#394eba")))

colors.append(ColorSet("mink", ColorDef("#7f7772", "#c5bdb9"), ColorHoverDef("#67605d", "#918b86"), ColorDef("#7f7772", "#bab2ad")))
colors.append(ColorSet("dark-mink", ColorDef("#201b1a", "#c5bdb9"), ColorHoverDef("#67605d", "#918b86"), ColorDef("#201b1a", "#bab2ad")))

colors.append(ColorSet("tortila", ColorDef("#997950", "#ecc890"), ColorHoverDef("#755d3f", "#9d885f"), ColorDef("#997950", "#ecc890")))
colors.append(ColorSet("dark-tortila", ColorDef("#20170f", "#ecc890"), ColorHoverDef("#20170f", "#9d885f"), ColorDef("#20170f", "#ecc890")))

colors.append(ColorSet("flax", ColorDef("#b5a35b", "#ffed8f"), ColorHoverDef("#6e6238", "#9f965a"), ColorDef("#b5a35b", "#ffed8f")))
colors.append(ColorSet("dark-flax", ColorDef("#201d0f", "#ffed8f"), ColorHoverDef("#6e6238", "#9f965a"), ColorDef("#201d0f", "#ffed8f")))

colors.append(ColorSet("brown", ColorDef("#523A28", "#A47551"), ColorHoverDef("#523A28", "#6e4f37"), ColorDef("#523A28", "#A47551")))
colors.append(ColorSet("dark-brown", ColorDef("#2f2316", "#A47551"), ColorHoverDef("#2f2316", "#6e4f37"), ColorDef("#2f2316", "#A47551")))

meta_template = None
with open("./template/meta-dark.html", "r") as fin:
    meta_template = fin.read()

for color in colors:
    meta_template = meta_template.replace("</head>", f"<style>\n{str(color)}</style>\n</head>")

with open("./template/dark.html", "w+") as fout:
    fout.write(meta_template)