# Bitmojify
Add a fun yet relevant bitmoji to your resumé because why not &amp; generate a LaTex preview for your resume 

##how do i use this epic script
1. Clone the libmoji repo onto your local machine: 
    `git clone https://github.com/matthewnau/libmoji.git`
    
2. Install with `npm install libmoji`
3. Run python script, `python3 bitmoji.py`
- This will generate a file, `resume.tex` which when compiled will have a random bitmoji at the top right corner 


##helpful repos/ how to contribute 
1. Use the doc2tex repo: `https://github.com/transpect/docx2tex`
- You can use this generate your own skeleton preview of the latex file. With this, you can simply replace the `skeleton.tex` file
so that it actually generates a resumé tailored to you :)

2. If the python script generates the following error: `SSL: CERTIFICATE_VERIFY_FAILED`, 
navigate to your python3.8 folder and run the following scripts by simply clicking on them:
`Install Certificates.command` and
`Update Shell Profile.command`

- If you'res still running into issues with this, check this answer out on [StackOverflow] {https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org
} 

