import hendr
import markdown

template = hendr.read_standard_template("dark")

mk_text = """
Very nice list:

* Markdown list item
* Markdown list item
* Markdown list item
* Markdown list item
"""

panel_content = hendr.TopPanelContent(
    hendr.PanelContent(["major top panel left"], ["major top panel right"]),
    [
        hendr.PanelContent(["minor top panel left"], ["minor top panel right"])
    ]
)

body_renders = [
    # hendr.TableRowRender(["Variable", "Value", "Description", "Comment"], ["15%", "15%", "60%", "8%"], "row tableHeader"),
    # hendr.TableRowRender(["disconnection.delay", "500ms", "Delay after disconnection", "..."], ["15%", "15%", "60%", "8%"], "row table"),
    # hendr.TableRowRender(["disconnection.counter", "10", "Count of retries", "..."], ["15%", "15%", "60%", "8%"], "row table"),
    # hendr.TableRowRender(["long.mk.description", "-", markdown.markdown(mk_text), "..."], ["15%", "15%", "60%", "8%"], "row table")

    hendr.TopPanelRender(panel_content),

    hendr.SpacerRender(),

    hendr.TableRowRender(
        [
            hendr.ColumnRender("Variable", "", "min-width: 15%"),
            hendr.ColumnRender("Value", "", "min-width: 15%"),
            hendr.ColumnRender("Description", "", "min-width: 60%"),
            hendr.ColumnRender("Comment", "", "min-width: 8%"),
        ],
    "row tableHeader"),

    hendr.TableRowRender(
        [
            hendr.ColumnRender("disconnection.delay", "", "min-width: 15%"),
            hendr.ColumnRender("500ms", "", "min-width: 15%"),
            hendr.ColumnRender("Delay after disconnection", "", "min-width: 60%"),
            hendr.ColumnRender("<a href=\"www.zive.cz\">link</a>", "", "min-width: 8%"),
        ],
        "row table"),

    hendr.TableRowRender(
        [
            hendr.ColumnRender("disconnection.counter", "", "min-width: 15%"),
            hendr.ColumnRender("10", "", "min-width: 15%"),
            hendr.ColumnRender("Count of retries", "", "min-width: 60%"),
            hendr.ColumnRender("...", "", "min-width: 8%"),
        ],
        "row table"),

    hendr.TableRowRender(
        [
            hendr.ColumnRender("long.mk.description", "", "min-width: 15%"),
            hendr.ColumnRender("-", "", "min-width: 15%"),
            hendr.ColumnRender(markdown.markdown(mk_text), "", "min-width: 60%"),
            hendr.ColumnRender("...", "", "min-width: 8%"),
        ],
        "row table"),

    hendr.SpacerRender(),

    hendr.TableRowRender(
        [
            hendr.ColumnRender("#", "", "width: 5%"),
            hendr.ColumnRender("Source", "", "width: 10%"),
            hendr.ColumnRender("Row", "", "width: 70%"),
            hendr.ColumnRender("Comment", "", "width: 13%"),
        ],
        "row tableHeader"),
    #
    # hendr.TableRowRender(
    #     [
    #         hendr.ColumnRender("1", "", "width: 5%"),
    #         hendr.ColumnRender("charon", "", "width: 10%"),
    #         hendr.ColumnRender("Reading certificates", "", "width: 70%"),
    #         hendr.ColumnRender(hendr.TextBoxRender("red box", "red"), "", "width: 13%"),
    #     ],
    #     "row notHighlighted"),
    #
    # hendr.TableRowRender(
    #     [
    #         hendr.ColumnRender("2", "", "width: 5%"),
    #         hendr.ColumnRender("charon", "", "width: 10%"),
    #         hendr.ColumnRender("Reading CRL", "", "width: 70%"),
    #         hendr.ColumnRender("Very long comment .... ....... ....... ........ ........... .........", "", "width: 13%;"),
    #     ],
    #     "row notHighlighted"),
    #
    # hendr.TableRowRender(
    #     [
    #         hendr.ColumnRender("3", "", "width: 5%"),
    #         hendr.ColumnRender("charon", "", "width: 10%"),
    #         hendr.ColumnRender("Error. Panic Panic Panic Panic Panic Panic Panic Panic It is time to be crazy !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Panic Panic Panic Panic Panic Panic Panic Panic", "", "width: 70%"),
    #         hendr.ColumnRender(hendr.ToolTipRender("ToolTip", "Hidden tool tip", "red", "width:300px"), "", "width: 13%;"),
    #     ],
    #     "row red"),
    #
    # hendr.TableRowRender(
    #     [
    #         hendr.ColumnRender("4", "", "width: 5%"),
    #         hendr.ColumnRender("charon", "", "width: 10%"),
    #         hendr.ColumnRender("Average row", "", "width: 70%"),
    #         hendr.ColumnRender(
    #             hendr.ToolTipRender(hendr.TextBoxRender("ToolTip", "red"), "Hidden tool tip 2", "", "width:300px"),
    #             "",
    #             "width: 13%;"
    #         ),
    #     ],
    #     "row notHighlighted"),
    #
    # hendr.TableRowRender(
    #     [
    #         hendr.ColumnRender("-", "", "width: 5%"),
    #         hendr.ColumnRender("-", "", "width: 10%"),
    #         hendr.ColumnRender("-", "", "width: 70%"),
    #         hendr.ColumnRender("-", "", "width: 13%;"),
    #     ],
    #     "row notHighlighted"),
    #
    # hendr.TableRowRender(
    #     [
    #         hendr.ColumnRender("-", "", "width: 5%"),
    #         hendr.ColumnRender("-", "", "width: 10%"),
    #         hendr.ColumnRender("-", "", "width: 70%"),
    #         hendr.ColumnRender("-", "", "width: 13%;"),
    #     ],
    #     "row notHighlighted"),

]

colors = [
    "red", "dark-red",
    "green", "dark-green",
    "blue", "dark-blue",
    "yellow", "dark-yellow",
    "gray", "dark-gray",
    "violet", "dark-violet",
    "orange", "dark-orange",
    "pink", "dark-pink",
    "cyan", "dark-cyan",
    "navy", "dark-navy",
    "mink", "dark-mink",
    "tortila", "dark-tortila",
    "flax", "dark-flax",
    "brown", "dark-brown"
]

for color in colors:
    body_renders += [
        hendr.TableRowRender(
            [
                hendr.ColumnRender("-", "", "width: 5%; padding-left:2px"),
                hendr.ColumnRender("-", "", "width: 10%"),
                hendr.ColumnRender("-", "", "width: 70%"),
                hendr.ColumnRender("<a href=\"www.zive.cz\">link</a>", "", "width: 13%;"),
            ],

            "row notHighlighted"),

        hendr.TableRowRender(
            [
                hendr.ColumnRender("-", "", "width: 5%; padding-left:2px"),
                hendr.ColumnRender("-", "", "width: 10%"),
                hendr.ColumnRender(hendr.TextBoxRender(f"Colored {color} text box", color), "", "width: 70%"),
                hendr.ColumnRender("<a href=\"www.zive.cz\">link</a>", "", "width: 13%;"),
            ],

            "row notHighlighted"),

        hendr.TableRowRender(
            [
                hendr.ColumnRender("0", "", "width: 5%; padding-left:2px;"),
                hendr.ColumnRender("source", "", "width: 10%;"),
                hendr.ColumnRender(color, "", "width: 70%;"),
                hendr.Container([
                    hendr.ColumnRender(hendr.ToolTipRender(hendr.TextBoxRender(f"Colored {color} text box", color),
                                                           f"Colored {color} text box tool tip <a href=\"www.zive.cz\">link</a> Some text .... Text text text wrap text ... <br/> text",
                                                           color,
                                                           "width:800px"
                                                           ),
                                       color,
                                       ""), # width: 13%; vertical-align: center;
                    "<a href=\"www.zive.cz\">link</a>"
                ])
            ],
            f"row {color}"),
    ]

for color in [color for color in colors if "dark" not in color]:
    body_renders += [
        hendr.TableRowRender(
            [
                hendr.ColumnRender("-", "", "width: 5%; padding-left:2px"),
                hendr.ColumnRender("-", "", "width: 10%"),
                hendr.ColumnRender("-", "", "width: 70%"),
                hendr.ColumnRender("<a href=\"www.zive.cz\">link</a>", "", "width: 13%;"),
            ],
            "row notHighlighted"),

        hendr.TableRowRender(
        [
            hendr.ColumnRender("-", "", "width: 5%; padding-left:2px"),
            hendr.ColumnRender("-", "", "width: 10%"),
            hendr.ColumnRender(f"<span class=\"text-{color}\"> Colored Text</span>", "", "width: 70%"),
            hendr.ColumnRender("<a href=\"www.zive.cz\">link</a>", "", "width: 13%;"),
        ],
        "row notHighlighted"),

        hendr.TableRowRender(
            [
                hendr.ColumnRender("-", "", "width: 5%; padding-left:2px"),
                hendr.ColumnRender("-", "", "width: 10%"),
                hendr.ColumnRender("-", "", "width: 70%"),
                hendr.ColumnRender("<a href=\"www.zive.cz\">link</a>", "", "width: 13%;"),
            ],
            "row notHighlighted"),

        hendr.TableRowRender(
            [
                hendr.ColumnRender("0", "", "width: 5%; padding-left:2px;"),
                hendr.ColumnRender("source", "", "width: 10%;"),
                hendr.ColumnRender(color, "", "width: 70%;"),
                hendr.Container([
                    hendr.ColumnRender(hendr.TextBoxRender(f"Colored {color} text box", color), color, ""),
                    "<a href=\"www.zive.cz\">link</a>"
                ]),
            ],
            f"row dark-{color}"),

    ]

body_renders += [
    hendr.TableRowRender(
        [
            hendr.ColumnRender("-", "", "width: 5%; padding-left:2px"),
            hendr.ColumnRender("-", "", "width: 10%"),
            hendr.ColumnRender("-", "", "width: 70%"),
            hendr.ColumnRender("<a href=\"www.zive.cz\">link</a>", "", "width: 13%;"),
        ],

        "row notHighlighted"),

    hendr.TableRowRender(
        [
            hendr.ColumnRender("0", "", "width: 5%; padding-left:2px;"),
            hendr.ColumnRender("source", "", "width: 10%;"),
            hendr.ColumnRender(color, "", "width: 70%;"),
            hendr.ColumnRender(
                hendr.TextBoxRender(f"Colored dark-gray text box", "dark-gray"),
                color,
                "width: 13%; vertical-align: center;"),
        ],
        f"row dark-gray"),

    hendr.ToolTipRender(hendr.TextBoxRender(f"Colored {color} text box", color),
                                                           f"Colored {color} text box tool tip <a href=\"www.zive.cz\">link</a> Some text .... Text text text wrap text ... <br/> text",
                                                           color,
                                                           "width:800px"
                                                           ),

]

body_renders += [
    hendr.SpacerRender(),
    hendr.BottomPanelRender(["bottom panel left", "bottom panel right"])
]

page = hendr.render(template, body_renders, "Super Fake Title")
hendr.save(page, "test.html")
