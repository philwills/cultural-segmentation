<html>
<form>
<input type="text" name="name" />
<input type="submit" />
</form>
{% if ward %}
	{{ ward.name }} ({{ ward.district }})
	<b>{{ ward.biggest }}</b>
{% endif %}
</html>
