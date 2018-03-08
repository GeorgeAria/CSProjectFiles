<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Admin Page</title>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet"
	href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
</head>
<body>

	<table class="table table-striped table-bordered">
		<thead>
			<tr>
				<th>Quotation</th>
				<th>Author</th>
				<th>Times Viewed</th>
				<th>Remove Links</th>
			</tr>
		</thead>

		<tbody>
			<c:forEach items="${quotes}" var="quote">
				<tr>
					<th>${quote.quote}</th>
					<th>${quote.author}</th>
					<th>${quote.timesViewed}</th>
					<th><a
						href="/cs320stu02/Final/RemoveQuotation?quote=${quote.quote}">
							Remove </a></th>

				</tr>
			</c:forEach>

		</tbody>

	</table>
	
	
	 
	<div class="container">
	<h1>
	 Add User 
	 </h1>
		<form action="QuoteAdmin" method="post">

			<div style="float: left">
				<c:out value="Author" />
				<div class="form-group">
					<input type="text" class="form-control" name="author" />
				</div>
				<c:out value="Quote" />
				<div class="form-group">
					<input type="text" class="form-control" name="quote" />
				</div>
			</div>

			<div style="float: right">
				<button type="submit" class="btn btn-primary">Add Quotation</button>
			</div>
		</form>
	</div>
	
	<a href = "/cs320stu02/Final/RandomQuote">
	<button class = "btn btn-primary">
		Click for Random Quote		
	</button>
	</a>


</body>
</html>