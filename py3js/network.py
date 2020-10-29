from importlib import resources
import json
from typing import List
import base64


class Node:
    def __init__(self,
                 id: str,
                 label: str = None,
                 tooltip: str = None,
                 color: str = "black", level: int = None,
                 radius: int = 8,
                 stroke_color: str = "black",
                 stroke_width: int = 1):
        self.id = id
        self.label = label
        self.tooltip = tooltip or label
        self.color = color
        self.level = level
        self.radius = radius
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width


class Link:
    def __init__(self, source: str, target: str, color: str = "orange",
                 opacity: float = 1.0,
                 width: float = 1,
                 is_arrow: bool = True):
        self.id = 0
        self.source = source
        self.target = target
        self.color = color
        self.opacity = opacity
        self.width = width
        self.is_arrow = is_arrow


class ForceDirectedGraph:

    def __init__(self, width: int = 800, height: int = 600,
                 x_levels: int = -1,
                 collision_radius: int = 8,
                 link_type: str = "link"):
        self._html = resources.read_text("py3js", "force.html")
        self._html = (self._html
                      .replace("$width", str(width))
                      .replace("$height", str(height))
                      .replace("$x_levels", str(x_levels))
                      .replace("$collision_radius", str(collision_radius))
                      .replace("$linkType", link_type))
        self._width = width
        self._height = height

        self._nodes: List[Node] = []
        self._links: List[Link] = []

        self._link_id_i = 0;

    def add_nodes(self, *node: Node):
        for n in node:
            self._nodes.append(n)

    def add_links(self, *link: Link):
        for lnk in link:
            lnk.id = self._link_id_i
            self._link_id_i += 1
            self._links.append(lnk)

    def _render_data(self):
        r = self._html

        nodes = [{
            "id": n.id,
            "label": n.label,
            "tooltip": n.tooltip,
            "color": n.color,
            "level": n.level,
            "radius": n.radius,
            "stroke": n.stroke_color,
            "stroke_width": n.stroke_width
        } for n in self._nodes]

        links = [{
            "id": l.id,
            "source": l.source,
            "target": l.target,
            "color": l.color,
            "opacity": l.opacity,
            "width": l.width,
            "arrow": l.is_arrow
        } for l in self._links]

        nodes_json = json.dumps(nodes)
        links_json = json.dumps(links)

        r = (r
             .replace("$data_nodes", nodes_json)
             .replace("$data_links", links_json))
        return r

    def _repr_html_(self):
        data = self._render_data()
        b64data = base64.b64encode(data.encode("utf-8")).decode("utf-8")
        url = f"data:text/html;charset=utf-8;base64,{b64data}"
        return f"<iframe src=\"{url}\" width=\"{self._width}\" height=\"{self._height}\" scrolling=\"no\" style=\"border:none !important;\"></iframe>"



    def save(self, path: str):
        with open(path, "w") as writer:
            writer.write(self._repr_html_())
