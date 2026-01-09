import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import app

def test_header_present(dash_duo):
    dash_duo.start_server(app.app)
    header = dash_duo.find_element("h1")
    assert header.text != ""


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app.app)
    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app.app)
    radio = dash_duo.find_element("#region-picker")
    assert radio is not None