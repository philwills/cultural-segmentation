<html>
<form>
<input type="text" name="name" />
<input type="submit" />
</form>
{% if ward %}
	{{ ward.name }}
{% endif %}
</html>
