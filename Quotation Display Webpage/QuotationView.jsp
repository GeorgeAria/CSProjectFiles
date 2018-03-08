<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Quotation View Page</title>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet"
	href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
</head>
<body>
<div class = "container">
	<h1>
		<c:out value = 'Here\'s a random quote for you'/>
	</h1>
	
	<h3>
		<c:out value =  'Quote:  ${theQuote.quote} '/>
	</h3>
	
	<h3>   
		<c:out value =  'Author:  ${theQuote.author}'/>
	</h3>	
	
	<h2>
		<c:out value = '${message}'/>
	</h2>
	
	<a href = "/cs320stu02/Final/RandomQuote">
	<button class = "btn btn-primary">
		Click for Random Quote		
	</button>
	</a>
	
	<a href = "/cs320stu02/Final/QuoteAdmin">
	<button class = "btn btn-primary">
		Add/Remove Quotations		
	</button>
</a>
	
</div>



	

</body>
</html>