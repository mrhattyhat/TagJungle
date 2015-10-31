{% extends 'base.tpl' %}

{% block title %}You suck{% endblock %}

{% block main %}
    <form name="search_form" method="post" action="phone_search">
        <input type="text" name="url"/>
        <input type="submit" name="search" value="Search"/>
    {% csrf_token %}
    </form>
    {% for number in numbers %}
        <div>
            <div style="display: inline-block">Phone Number</div>
            <div style="display: inline-block">{{ number.number }}</div>
        </div>
    {% endfor %}

{% endblock %}
</form>