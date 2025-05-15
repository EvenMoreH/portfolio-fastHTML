from fasthtml.common import * # type: ignore

# for Docker
app, rt = fast_app(static_path="static") # type: ignore

# for local
# app, rt = fast_app(static_path="app/static") # type: ignore


@rt("/")
def homepage():
    return Html(
        Head(
            Title("Fast Tools Hub"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Script(src="https://unpkg.com/htmx.org"),
            Link(rel="stylesheet", href="css/tailwind.css"),
            Link(rel="icon", href="images/favicon.ico", type="image/x-icon"),
            Link(rel="icon", href="images/favicon.png", type="image/png"),
        ),
        Body(
            Div(
                Div(
                    H1("Welcome", cls="text-3xl md:text-5xl font-bold mb-4 md:pb-2 pb-0.5 text-center xl:text-center "),
                    P(paragraph, cls="text-gray-200 md:text-lg text-left xl:text-center"),
                    cls="md:w-1/2 mb-8 md:mb-0"
                ),
                cls="container mx-auto px-6 flex flex-col md:flex-row items-center justify-center pt-4 md:pt-3"
            ),
            Div(cls="pb-[1vw] md:pb-[2vw]"),
            Div(
                Div(
                    H3("Alarm!",
                        cls="grid-title"),
                    Div(
                        Img(src="images/free-clock-sq.ico",
                            type="image/png",
                            alt="fastalarm", cls="img"),
                        cls="img-container"
                    ),
                    P(description_alarm,
                        cls="text-gray-200"),
                    hx_get="/alarm",
                    cls="grid-tile",
                ),
                Div(
                    H3("Temperature Converter",
                        cls="grid-title"),
                    Div(
                        Img(src="images/temperature-converter-sq2.ico",
                            type="image/png",
                            alt="tempconverter", cls="img"),
                        cls="img-container"
                        ),
                    P(description_temperature,
                        cls="text-gray-200"),
                    hx_get="/temperature",
                    cls="grid-tile",
                ),
                Div(
                    H3("QR Code Generator",
                        cls="grid-title"),
                    Div(
                        Img(src="images/qrcode.ico",
                            type="image/png",
                            alt="qrcodegen", cls="img"),
                        cls="img-container"
                        ),
                    P(description_qr,
                        cls="text-gray-200"),
                    hx_get="/qr-gen",
                    cls="grid-tile",
                ),
                Div(
                    H3("TTRPG Distance Converter",
                        cls="grid-title"),
                    Div(
                        Img(src="images/running-distance.ico",
                            type="image/png",
                            alt="ttrpgdistance", cls="img"),
                        cls="img-container"
                        ),
                    P(description_distance,
                        cls="text-gray-200"),
                    hx_get="/distance_converter",
                    cls="grid-tile",
                ),
                Div(
                    H3("Dice Roller",
                        cls="grid-title"),
                    Div(
                        Img(src="images/favicon-roller2.ico",
                            type="image/png",
                            alt="diceroller", cls="img"),
                        cls="img-container"
                        ),
                        P(description_dice,
                        cls="text-gray-200"),
                    hx_get="/dice_roller",
                    cls="grid-tile",
                ),
                Div(
                    H3("Color Converter",
                        cls="grid-title"),
                    Div(
                        Img(src="images/splat1-noBG.ico",
                            type="image/png",
                            alt="color-converter", cls="img"),
                        cls="img-container"
                        ),
                        P(description_color,
                        cls="text-gray-200"),
                    hx_get="/color_converter",
                    cls="grid-tile",
                ),
                cls="container mx-auto px-3 md:px-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2 md:gap-8 max-w-[1200px]"
            ),
            Div(cls="pt-[3vw]"),
            Footer(
                Div(
                    A("by EvenMoreH", href="https://github.com/EvenMoreH", cls="text-gray-350"),
                    cls="container mx-auto px-6 text-center hover:scale-125 transition-all duration-200"
                ),
                cls="bg-dark-theme-lightgray py-2 md:py-3 fixed bottom-0 w-full"
            ),
            cls="bg-dark-theme-gray text-gray-100 h-full"
        )
    )

@rt("/alarm")
def alarm():
    return Redirect("https://alarm.fastools.xyz")

@rt("/temperature")
def temperature():
    return Redirect("https://temperature.fastools.xyz")

@rt("/qr-gen")
def qr_generator():
    return Redirect("https://qr.fastools.xyz")

@rt("/distance_converter")
def distance_converter():
    return Redirect("https://distance.fastools.xyz")

@rt("/dice_roller")
def dice_roller():
    return Redirect("https://roll.fastools.xyz")

@rt("/color_converter")
def color_converter():
    return Redirect("https://color.fastools.xyz/")

paragraph = """
            Discover a sleek, dynamic tool hub crafted with Tailwind CSS.
            Navigate through a grid of tiles, each being a gateway leading to a tool I am using everyday.
            """

description_alarm = """
Timer with 4 separate instances - best for cooking!
"""
description_temperature = """
Fast and easy conversions between different temperature units
"""
description_qr = """
Simple QR Code Generator for your webpages
"""
description_distance = """
Simple distance converter for your hex and square based TTRPGs
"""
description_dice = """
Click-by-click dice roller for your TTRPGs
"""
description_color = """
Convert your colors between TailwindCSS, hex and RGBA
"""


if __name__ == '__main__':
    # Important: Use host='0.0.0.0' to make the server accessible outside the container
    serve(host='0.0.0.0', port=5050) # type: ignore
