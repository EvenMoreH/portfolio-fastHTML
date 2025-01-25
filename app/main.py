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
                    H1("Welcome", cls="text-3xl md:text-5xl font-bold mb-4 md:p-b-var-pad-2 p-b-var-pad-1"),
                    P(paragraph, cls="text-gray-200 md:text-lg"),
                    cls="md:w-1/2 text-center md:text-center mb-8 md:mb-0"
                ),
                cls="container mx-auto px-6 flex flex-col md:flex-row items-center justify-center p-t-var-pad-2 md:p-t-var-pad-3"
            ),
            Div(cls="p-b-var-pad-1 md:p-b-var-pad-2 xl:p-b-var-pad-3 xxl:p-b-var-pad-4"),
            Div(
                Div(
                    H3("Fast Alarm",
                        cls="grid-title"),
                    Img(src="images/fastalarm.png",
                        type="image/png",
                        alt="fastalarm", cls="hidden lg:block max-w-64 xl:max-w-72 h-auto mx-auto pb-0.5"),
                    P("Timer with 4 separate instances - best for cooking!",
                        cls="text-gray-200"),
                    hx_get="/alarm",
                    cls="grid-tile",
                ),
                Div(
                    H3("Temperature Converter",
                        cls="grid-title"),
                    Img(src="images/tempconverter.png",
                        type="image/png",
                        alt="tempconverter", cls="hidden lg:block max-w-64 xl:max-w-72 h-auto mx-auto pb-0.5"),
                    P("Fast and easy conversions between different temperature units",
                        cls="text-gray-200"),
                    hx_get="/temperature",
                    cls="grid-tile",
                ),
                Div(
                    H3("QR Code Generator",
                        cls="grid-title"),
                    Img(src="images/qrcodegen.png",
                        type="image/png",
                        alt="qrcodegen", cls="hidden lg:block max-w-64 xl:max-w-72 h-auto mx-auto pb-0.5"),
                    P("Simple QR Code Generator for your webpages",
                        cls="text-gray-200"),
                    hx_get="/qr-gen",
                    cls="grid-tile",
                ),
                Div(
                    H3("TTRPG Distance Converter",
                        cls="grid-title"),
                    Img(src="images/ttrpgdistance.png",
                        type="image/png",
                        alt="ttrpgdistance", cls="hidden lg:block max-w-64 xl:max-w-72 h-auto mx-auto pb-0.5"),
                    P("Simple distance converter for your hex and square based TTRPGs",
                        cls="text-gray-200"),
                    hx_get="/distance_converter",
                    cls="grid-tile",
                ),
                Div(
                    H3("Dice Roller",
                        cls="grid-title"),
                    Img(src="images/diceroller.png",
                        type="image/png",
                        alt="diceroller", cls="hidden lg:block max-w-64 xl:max-w-72 h-auto mx-auto pb-0.5"),
                    P("Click-by-click dice roller for your TTRPGs",
                        cls="text-gray-200"),
                    hx_get="/dice_roller",
                    cls="grid-tile",
                ),
                cls="container mx-auto px-3 md:px-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2 md:gap-8"
            ),
            Div(cls="p-t-var-pad-3"),
            Footer(
                Div(
                    A("by EvenMoreH", href="https://github.com/EvenMoreH", cls="text-gray-350"),
                    cls="container mx-auto px-6 text-center hover:scale-125 transition-all duration-200"
                ),
                cls="bg-rose-950/20 py-3 md:py-5 fixed bottom-0 w-full"
            ),
            cls="bg-stone-950/95 text-gray-100"
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
def distance_converter():
    return Redirect("https://roll.fastools.xyz")

paragraph = """
            Discover a sleek, dynamic tool hub crafted with Tailwind CSS.
            Navigate through a grid of tiles, each being a gateway leading to a tool I am using everyday.
            """

if __name__ == '__main__':
    # Important: Use host='0.0.0.0' to make the server accessible outside the container
    serve(host='0.0.0.0', port=5050) # type: ignore