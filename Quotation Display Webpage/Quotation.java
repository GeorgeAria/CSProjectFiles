package cs320.finals;

public class Quotation 
{
	private String author;
	private String quote;
	private int timesViewed = 0;
	
	public Quotation()
	{
		
	}
	
	public Quotation(String author, String quote)
	{
		this.author = author;
		this.quote = quote;
	}
	
	public Quotation(String author, String quote, int timesViewed)
	{
		this.author = author;
		this.quote = quote;
		this.timesViewed = timesViewed;
	}

	public String getAuthor() {
		return this.author;
	}

	public void setAuthor(String author) {
		this.author = author;
	}

	public String getQuote() {
		return this.quote;
	}

	public void setQuote(String quote) {
		this.quote = quote;
	}

	public int getTimesViewed() {
		return this.timesViewed;
	}

	public void setTimesViewed(int timesViewed) {
		this.timesViewed = timesViewed;
	}
	
	

}
