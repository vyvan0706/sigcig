This is a blog i made for a project in my school, based mostly on css, html for design
#   html_content5 = """
# <div class="word"></div>
# """

# # Define the CSS styles
#   css_styles = """
# <style>
# html {
#   height: 100%;
# }

# .word {
#   margin: auto;
#   position:absolute;
#   top:250px;
#   left:80px;
#   color: black;
#   font: 700 normal 5em 'Eb Garamond';
#   text-shadow: 5px 2px #EBE3D5, 2px 4px #EBE3D5, 3px 5px #EBE3D5;
# }
# </style>
# """

# # Define the JavaScript code
#   javascript_code = """
# <script>
# var words = ["Hi I'm Lev", "I'm from Europe", "I'm currently working in London"],
#     part,
#     i = 0,
#     offset = 0,
#     len = words.length,
#     forwards = true,
#     skip_count = 0,
#     skip_delay = 15,
#     speed = 70;
# var wordflick = function () {
#   setInterval(function () {
#     if (forwards) {
#       if (offset >= words[i].length) {
#         ++skip_count;
#         if (skip_count == skip_delay) {
#           forwards = false;
#           skip_count = 0;
#         }
#       }
#     }
#     else {
#       if (offset == 0) {
#         forwards = true;
#         i++;
#         offset = 0;
#         if (i >= len) {
#           i = 0;
#         }
#       }
#     }
#     part = words[i].substr(0, offset);
#     if (skip_count == 0) {
#       if (forwards) {
#         offset++;
#       }
#       else {
#         offset--;
#       }
#     }
#     document.querySelector('.word').innerText = part;
#   },speed);
# };

# wordflick();
# </script>
# """
#   custom_component = f"{css_styles}\n{html_content5}\n{javascript_code}"
#   components.html(custom_component, height=500)