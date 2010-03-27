<html>
<form action="/" method="post">
<input type="text" name="postcode" />
<input type="submit" />
</form>
{% if ward %}
	{{ ward.name }} ({{ ward.district }})
	<b>{{ ward.biggest }}</b>
{% endif %}
</html>
