from typing import Callable
import pynecone as pc
from priconne_backend.route import Route


def content_page(path: str, title: str = "PriConne Mapping Project", props=None) -> Callable:
    """Template suitable for most pages on site. Includes header & footer."""
    props = props or {}
    
    def page(contents: Callable[[], Route]) -> Route:
        """Wrapper for a templated route."""
        def wrapper(*children, **props) -> pc.Component:
            """Returns component with template applied."""
            from priconne_backend.utils.header import header
            from priconne_backend.utils.footer import footer
            
            return pc.box(
                header(),
                contents(*children, **props),
                footer(),
                font_family="Inter",
                **props
            )
            
        return Route(path=path, title=title, component=wrapper)
    
    return page