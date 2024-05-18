import sys, threading
import eel
import webview


@eel.expose
def hello_world():
    print("Hello from python")


@eel.expose
def get_greeting(string):
    return f"hello {string}"


def start_app():
    eel_thread = threading.Thread(target=eel_start, daemon=True)
    eel_thread.start()
    webview_start()


def eel_start():
    eel.init("web")
    eel.start(
        "index.html",
        mode=None,
        # mode="default",
        # mode="chrome",
        host="localhost",
        port=27000,
        shutdown_delay=0.0,
    )


def webview_start():
    window_app = webview.create_window(
        "App",
        "http://localhost:27000/",
        frameless=False,
        # frameless=True,
        width=800,
        height=600,
        resizable=True,
        # resizable=False,
        fullscreen=False,
    )
    webview.start(window_app)


if __name__ == "__main__":
    # Dont forget to run "yarn build"
    start_app()
    print(" [EXIT]")
