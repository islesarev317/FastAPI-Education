def get_html_card(header, description):
    return f"""
<div class="card">
    <h1>{header}</h1>
    <p>{description}</p>
</div>
"""


def get_html_grid(word_set):
    cards = []
    for word, definition in word_set:
        cards.append(get_html_card(word, definition))
    grid = "\n".join(cards)
    page = f"""
 <!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Cards</title>
    <link rel="stylesheet" href="styles/grid.css">
</head>
<body>
<section class="card-container">
{grid}
</section>
</body>
"""
    return page

