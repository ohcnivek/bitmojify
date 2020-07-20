<p align="center">
  <img src="https://sdk.bitmoji.com/render/panel/485d05c9-806d-4a57-b680-1721063a96ef-3243472b-d164-4e1a-8510-6b5c56f686ed-v1.png?transparent=1&palette=1" />
</p>
# Bitmojify 
Add a fun yet relevant bitmoji to your resumé because why not &amp; generate a LaTex preview for your resume 

## Some things you'll need along the way
1. LaTex - why? Before the pdf of the resumé is generated, it is first a `.tex` file, which needs LaTex to be compile it.  
- Can be downloaded [here](https://www.latex-project.org/get/)

2. Node.js - why? `bitmoij.py` uses it to run `index.js` locally to retrieve the generated bitmoji
- Can be downloaded [here](https://nodejs.org/en/download/)

3. You _need_ Python3. Otherwise, an imported library (urllib.request) will cause issues

## How do I use this epic script?
1. Clone the libmoji repo onto your local machine: 
    `git clone https://github.com/matthewnau/libmoji.git`
    
2. Install with `npm install libmoji`
3. Run python script, `python3 bitmoji.py`
- This will generate a file, `myresume.tex` which when compiled to `myresume.pdf` (the script automatially does this) will have a random bitmoji on the top right corner 

## Other very helpful repos/ how to contribute 
1. Use the doc2tex repo: `https://github.com/transpect/docx2tex`
- With this, you can simply replace the `skeleton.tex` file with a new skeleton file that contains the contents of your resumé so that it actually generates a resumé tailored to you :) Maybe in the future, I'll find a way to integrate this into the project

2. If the python script generates the following error: `SSL: CERTIFICATE_VERIFY_FAILED`, 
navigate to your python3.8 folder and run the following scripts by simply clicking on them:
`Install Certificates.command` and
`Update Shell Profile.command`

- If you'res still running into issues with this, check this answer out on [StackOverflow](https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org)

