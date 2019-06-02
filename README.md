This is the script that updates https://github.com/cismirror/benchmarks repository. It is provided here so you can run your own copy if you want to. This is what it does:
- Runs headless chromium
- Goes to https://learn.cisecurity.org/benchmarks
- Fills in the form and submits it (the only field that matters is the email)
- Waits for a little bit for the email from CIS to arrive
- Gets the link from the email and goes to that page
- Downloads all benchamarks to a repo cloned from https://github.com/cismirror/benchmarks
- Commits and pushes any changed/added files to https://github.com/cismirror/benchmarks

You will need to figure out how to run it, because I can't be bothered to write a proper howto at the moment. Entry point is benchmarks.py.

If you do figure out how to run it and make any improvements - pull requests would be much appreciated. Some things that could be improved:
- Figure out how to get the benchamrks without using browser, e.g. by using requests library or something like that. Doing that would enable me to run this on aws fargate for the fraction of the price tha I'm paying for it right now.
- Figure out how to do git nativelly in python
