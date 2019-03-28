New York Times APIs
==================

If you are interested in easily downloading large amounts of data from the New York Times, this is the package for you. Technically, it is a set of Python wrappers for making calls to the New York Times APIs such as Archive, ArticleSearch, and others. 

It is still in development, so for now I'm working on the Archive API wrapper. When it is done, anyone will be able to go to the [New York Times developer site](https://developer.nytimes.com/), sign up for an API key, add the API to your project, and download all the articles for a certain month or all the articles ever published. I am not sure yet whether to make that a flag option to be specified from the command line, but the intention is to make downloading every article the New York Times has ever published as easy as possible. 

Later I will try to come out with a wrapper for the Article Search API, since other ones that are supposed to exit see to have been abandoned. 

For right now, though, the steps are as follows:

1. Visit the NYT developer website and [secure yourself an API key](https://developer.nytimes.com/get-started).
2. Clone `nytAPI` by typing 

```
$ https://github.com/chrisrytting/nytAPI.git
```
into the commandline. 

3. `cd` into `nytAPI`
4. Run the following command:

```
$ archiveAPI apikey month year
```

Following these steps will allow you to make a call to the API to download all the articles the New York Times published in the specified month and year. The download is saved as `response.json` and is obviously in JSON format. For now i'll leave it to you to parse through that JSON object to find what you're interested in, but there is plenty there (author, article content, different tags, etc.). 

Lastly, you can only make calls every 6 seconds, so make sure to wait long enough between calls.

Let me know if you have any questions!
