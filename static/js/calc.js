const calculate = () => {
	const val1 = $('#f1').val();
	const val2 = $('#f2').val();
	console.log('The value is ' + val1);
	console.log('The value is ' + val2);
	$.ajax({
		type: 'POST',
		url: '/parse_data',
		data: JSON.stringify({ release: val1, product: val2 }),
		contentType: 'application/json',
		success: function(data) {
			console.log(data);
			document.getElementById('results').innerHTML = data.results;
		}
	});
};
