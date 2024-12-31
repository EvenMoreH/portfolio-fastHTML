from fasthtml.common import * # type: ignore
from fasthtml.common import (
    Button, Html, Head, Body, Div, Title, Titled, A, Link, Meta
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
                    A(
                        "Fast Alarm",
                        href="https://alarm.fastools.xyz",
                        title="Timer with 4 separate instances - best for cooking!",
                    ),
                ),
                cls="container",
            ),
            Div(
                Button(
                    A(
                        "Temperature Converter",
                        href="https://temperature.fastools.xyz",
                        title="Fast and easy conversions between different temperature units.",
                    ),
                ),
                cls="container",
            )
        )
    )

if __name__ == '__main__':
    # Important: Use host='0.0.0.0' to make the server accessible outside the container
    serve(host='0.0.0.0', port=5050) # type: ignore