# regx for getting assets urls
"../../([A-Z a-z 0-9 / . -]*)"  
"../../plugins/([A-Z a-z 0-9 / . -]*)"

# regx for changing it to static
{% static '$1' %}