package cs320.finals;

import java.io.IOException;
import java.sql.Connection;
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Random;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;



@WebServlet("/Final/RandomQuote")
public class QuotationView extends HttpServlet {
	private static final long serialVersionUID = 1L;

	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException 
	{
		String username = "cs320stu02";
		String password = "HW*hR#.O";
				
		String host = "cs3.calstatela.edu";
		String port = "3306";
		String dbName = "cs320stu02";
		
		
		String url = "jdbc:mysql://" + host + ":" + port + "/" + dbName;
		
		try
		{
			//Dynamically include MYSQL driver
			System.out.println("Class.forName");
			Class.forName("org.gjt.mm.mysql.Driver").newInstance();
			
			//Instantiate the Driver
			Driver driver = new org.gjt.mm.mysql.Driver();
			
			//Connect to the Database
			System.out.println("Creating Connection");
			Connection connection = DriverManager.getConnection(url, username, password);
			
			//Create statement
			System.out.println("Creating Statement");
			Statement statement = connection.createStatement();
			
			//Create SQL query
			String query = "SELECT * FROM quotes";
			
			//Execute query
			ResultSet resultSet = statement.executeQuery(query);
			
			//Iterate over the results, and create models for the view
			ArrayList<Quotation> quotes = new ArrayList<Quotation>();
			String message = "";
			Random ran = new Random();
			
			System.out.println("Iterating over results");
			
			
			
				while(resultSet.next())
				{
					String author = resultSet.getString("author");
					String quote = resultSet.getString("quote");
					int timesViewed = resultSet.getInt("timesViewed");
					quotes.add(new Quotation(author, quote, timesViewed));
				}
				
			int index = ran.nextInt(quotes.size());
			Quotation theQuote = quotes.get(index);
			if(theQuote.getTimesViewed() == 0)
			{
				message = "You are the first person to view this quotation";
				theQuote.setTimesViewed(theQuote.getTimesViewed() + 1);
			}
			else
			{
				message = "This quotation has been viewed " + theQuote.getTimesViewed() + " times.";
				theQuote.setTimesViewed(theQuote.getTimesViewed() + 1);
			}
			
			String query2 = "UPDATE quotes SET timesViewed = '" + theQuote.getTimesViewed() + "' WHERE quote = '" + theQuote.getQuote() + "'";
			
			int i = statement.executeUpdate(query2);
			
					
			
			//Tidy up
			connection.close();
			
			//Attach the results to the Request object
			request.setAttribute("theQuote", theQuote);
			request.setAttribute("message", message);
			
			//Forward the request and response to the view
			System.out.println("Dispatching");
			request.getRequestDispatcher("/WEB-INF/final/QuotationView.jsp").forward(request, response);
		}
		
		catch(Exception e)
		{
			System.out.println(e.getLocalizedMessage());
		}
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException 
	{
		doGet(request, response);
	}

}
