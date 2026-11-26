# Explore the omitted parent

[Download the offline explorer ZIP](https://raw.githubusercontent.com/DannyExperiments/cp-net-aggregation-sharp-ratio/v1.0.0/visualization/cp-net-aggregation-sharp-ratio-explorer.zip), extract it, and open index.html in a browser. Select a hidden attribute, change the visible bits, or rotate the two context cubes. Each cube contains the same eight visible settings. Its hidden bit takes the value in its heading.

For the all-zero visible setting with X1 hidden, the highlighted contexts are 0000 and 1000. Their respective votes for 1 are 0 and 3, so output 0 costs 3 disagreements and output 1 costs 5. When exactly one visible bit is 1, the paired counts are 3 and 4, and output 1 costs only 1. Each pair has a unique minimizing output. Across all contexts, full majority costs 4 while each restricted minimizer costs 6.

Point colors denote the number of votes for 1. Gray indicates 0, blue 3, and mint 4. Amber identifies the highlighted pair. The GIF alternates two visible settings for fixed hidden X1. The four-attribute context cube is shown as two rotating three-dimensional slices. [General proof](../paper/manuscript.pdf)

To render the GIF, use an existing Python environment with Pillow and Arial or DejaVu Sans available.

    python3 visualization/render.py
