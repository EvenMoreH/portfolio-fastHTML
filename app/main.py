from fasthtml.common import * # type: ignore
from fasthtml.common import (
    Button, Html, Head, Body, Div, Title, Titled, A, Link, Meta, RedirectResponse
)

# for docker
app, rt = fast_app(static_path="static") # type: ignore

# for local
# app, rt = fast_app(static_path="app/static") # type: ignore


@rt("/")
def homepage():
    return Html(
        Head(
            Title("Fast Tools Hub"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Script("""
                function alarmPage() {
                        window.location.href = "/alarm";
                   }
                   """),
            Script("""
                function temperaturePage() {
                        window.location.href = "/temperature";
                   }
                   """),
            Link(rel="stylesheet", href="styles.css"),
            Link(rel="icon", href="images/favicon.ico", type="image/x-icon"),
            Link(rel="icon", href="images/favicon.png", type="image/png"),
        ),
        Body(
            Div(
                Titled("Select an app", cls="title"),
                cls="container",
            ),
            Div(
                Button(
                    "Fast Alarm",
                    onclick="alarmPage()",
                    title="Timer with 4 separate instances - best for cooking!",
                ),
                cls="container",
            ),
            Div(
                Button(
                    "Temperature Converter",
                    onclick="temperaturePage()",
                    title="Fast and easy conversions between different temperature units.",
                ),
                cls="container",
            )
        )
    )

@rt("/alarm")
def alarm():
    return RedirectResponse("https://alarm.fastools.xyz", status_code=302)

@rt("/temperature")
def temperature():
    return RedirectResponse("https://temperature.fastools.xyz", status_code=302)

if __name__ == '__main__':
    # Important: Use host='0.0.0.0' to make the server accessible outside the container
    serve(host='0.0.0.0', port=5050) # type: ignore