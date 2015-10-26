{% extends 'base.tpl' %}

{% block title %}You suck{% endblock %}

{% block main %}
    <form name="search_form" method="get" action="search">
        <input type="text" name="s"/>
        <select name="t">
            <option value="1">Person</option>
            <option value="2">Organization</option>
        </select>
        <input type="submit" name="search" value="Search"/>
    </form>

    <div id="results">
        {% for adj in adjectives %}
            <div>{{ adj }}</div>
        {% endfor %}
    </div>
{% endblock %}
</form>