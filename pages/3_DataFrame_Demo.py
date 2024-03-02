import streamlit.components.v1 as components
import streamlit as st
# Define the HTML content
html_content2 = """
<div class="word"></div>
"""

# Define the CSS styles
css_styles = """
<style>
html {
  height: 100%;
}

.word {
  margin: auto;
  top: 250px; /* Adjust the top position as needed */
  left: 200px;
  color: black;
  font: 700 normal 2.5em 'Eb Garamond';
  # text-shadow: 5px 2px #222324, 2px 4px #222324, 3px 5px #222324;
}
</style>
"""

# Define the JavaScript code
javascript_code = """
<script>
var words = ["Hi I'm Lev", "I'm from Europe", "I'm currently working in London"],
    part,
    i = 0,
    offset = 0,
    len = words.length,
    forwards = true,
    skip_count = 0,
    skip_delay = 15,
    speed = 70;
var wordflick = function () {
  setInterval(function () {
    if (forwards) {
      if (offset >= words[i].length) {
        ++skip_count;
        if (skip_count == skip_delay) {
          forwards = false;
          skip_count = 0;
        }
      }
    }
    else {
      if (offset == 0) {
        forwards = true;
        i++;
        offset = 0;
        if (i >= len) {
          i = 0;
        }
      }
    }
    part = words[i].substr(0, offset);
    if (skip_count == 0) {
      if (forwards) {
        offset++;
      }
      else {
        offset--;
      }
    }
    document.querySelector('.word').innerText = part;
  },speed);
};

wordflick();
</script>
"""

# Combine HTML, CSS, and JavaScript into a single component
custom_component = f"{css_styles}\n{html_content2}\n{javascript_code}"

# Render the custom component
components.html(custom_component, height=500)
