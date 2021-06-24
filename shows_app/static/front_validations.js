function validateForm(){

	
	//  USO DE EXPRESIONES REGULARES
	const SOLO_LETRAS = new RegExp(/^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$/);
	const PRIMERA_MAYUSCULA = new RegExp(/^[A-Z][a-z]+$/);
	const EMAIL_VALIDO = new RegExp(/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/);
	const VALIDAR_RUT = new RegExp(/^\d{1,2}\.\d{3}\.\d{3}[-][0-9kK]{1}$/);

	//array para validar que no se ingreses determinadas palabras o num
	const palabras_inseguras = [ "password" , "123456" , "0987654"];

	//obtengo datos ingresados, en un objeto en vez de crear una var para cada uno
	let datos={
		title : $("#title").val(), //cajita por el id, valor con .val()
		network : $("#network").val(),
		releaseDate : $("#release").val(),
		description : $("#description").val(),
	
	}

	//valido title
	if(datos.title == ""){	
		$("#title").after("<span class='alerta'>Title is required</span>");	

	}else if (PRIMERA_MAYUSCULA.test(datos.title) == false){
		$("#title").after("<span class='alerta'>First letter must be Uppercase</span>");
	}

    //valido network
	if(datos.network == "0"){
		$("select").after("<span class='alerta'>Add a network is required</span>");
	}

	//valido la descripcion
	if (SOLO_LETRAS.test(datos.description) == false){
		$("#description").after("<span class='alerta'>Only alphabetical characters</span>");

	}else if (PRIMERA_MAYUSCULA.test(datos.description) == false){
		$("#description").after("<span class='alerta'>First letter must be Uppercase</span>");
	}

		

}