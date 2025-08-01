from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

faqs = {
    "ai general chatbot": "chatgpt.com",
    "ai specialized about a youtube video or websites or your content": "notebooklm.google",
    "a large library for ui elements": "uiverse.io",
    "watch longer videos about everything": "youtube.com",
    "open source projects": "github.com",
    "buy me a coffee website to donate": "buymeacoffee.com/ivocreator",
    "mail from google": "gmail.com",
    "github readme stats": "gh-stats-gen.vercel.app/",
    "free code sandbox and hosting": "replit.com",
    "online code editor with preview": "glitch.com",
    "ai image generator by openai": "openai.com/dall-e",
    "ai voice tool by elevenlabs": "elevenlabs.io",
    "ai-generated video creation": "pika.art",
    "learning coding interactively": "codecademy.com",
    "website to learn anything with short summaries": "khanacademy.org",
    "ai slide maker and document generator": "gamma.app",
    "free online whiteboard": "figjam.new",
    "figma for design": "figma.com",
    "generate ui with ai": "uizard.io",
    "website builder with ai help": "durable.co",
    "api testing tool": "postman.com",
    "get free public apis": "rapidapi.com",
    "ai search assistant": "perplexity.ai",
    "ai image-to-website builder": "durable.co",
    "website with free css components": "tailwindcomponents.com",
    "tailwind css documentation": "tailwindcss.com",
    "programming q&a": "stackoverflow.com",
    "free font website": "fonts.google.com",
    "color palettes and ideas": "coolors.co",
    "remove background from images": "remove.bg",
    "compress images online": "tinypng.com",
    "make simple gifs online": "ezgif.com",
    "text-to-speech ai tool": "play.ht",
    "explore datasets for ai or ml": "kaggle.com",
    "ai tools directory": "theresanaiforthat.com",
    "simple pastebin tool": "pastebin.com",
    "host your static website free": "vercel.com",
    "version control help site": "git-scm.com",
    "online file converter": "cloudconvert.com",
    "build mobile apps with drag and drop": "thunkable.com",
    "free icon library": "fontawesome.com",
    "open source icon sets": "heroicons.com",
    "learn machine learning basics": "mlcourse.ai",
    "interactive python tutorials": "learnpython.org",
    "free online linux terminal": "jslinux.online",
    "free vpn service list": "vpnmentor.com",
    "free stock photos": "unsplash.com",
    "free stock videos": "pexels.com/videos",
    "free music for projects": "freemusicarchive.org",
    "website performance testing": "gtmetrix.com",
    "domain name checker": "namemesh.com",
    "seo tools free": "moz.com/free-seo-tools",
    "online mind mapping tool": "miro.com",
    "free blogging platform": "wordpress.com",
    "free email marketing": "mailchimp.com",
    "online survey maker": "google.com/forms",
    "free online pdf editor": "pdfescape.com",
    "website uptime monitoring": "uptimerobot.com",
    "learning platform for math": "brilliant.org",
    "free virtual events platform": "hopin.com",
    "simple crm for small business": "hubspot.com",
    "collaborative document editor": "notion.so",
    "todo list and project planner": "trello.com",
    "free webinars and tutorials": "coursera.org",
    "free domain email": "zoho.com/mail",
    "image color picker": "imagecolorpicker.com",
    "css animation generator": "animista.net",
    "markdown editor online": "stackedit.io",
    "free ssl certificates": "letsencrypt.org",
    "online json formatter": "jsonformatter.org",
    "free cloud storage": "google.com/drive",
    "open data repository": "data.gov",
    "free vpn test tools": "ipleak.net",
    "ai writing assistant": "grammarly.com",
    "git gui client": "gitkraken.com",
    "task automation platform": "ifttt.com",
    "free online courses for coding": "freecodecamp.org",
    "online qr code generator": "qr-code-generator.com",
    "free lorem ipsum generator": "lipsum.com",
    "website color contrast checker": "contrastchecker.com",
    "free podcast hosting": "anchor.fm",
    "open source operating systems": "ubuntu.com",
    "ai voice recognition": "speech-to-text-demo.ng.bluemix.net",
    "learn data science": "dataschool.io",
    "free virtual machines": "azure.microsoft.com/free",
    "learn graphic design": "canva.com/learn",
    "free vpn comparison": "thatoneprivacysite.net",
    "free online photo editor": "pixlr.com",
    "free ssl test": "ssllabs.com/ssltest",
    "open source video editor": "shotcut.org",
    "ai face generator": "thispersondoesnotexist.com",
    "learn javascript basics": "javascript.info",
    "free collaboration tool": "slack.com",
    "open source browsers": "mozilla.org/firefox",
    "simple chatbot platform": "dialogflow.cloud.google.com",
    "free code snippet manager": "gist.github.com",
    "free email testing tool": "mailtrap.io",
    "ai code generation": "github.com/features/copilot",
    "free domain email forwarding": "improvemail.com",
    "free digital marketing tools": "ubersuggest.com",
    "free ux research tools": "usertesting.com",
    "open source cms": "wordpress.org",
    "free serverless functions": "netlify.com/functions",
    "free api mocking": "beeceptor.com",
    "free app analytics": "firebase.google.com/products/analytics",
    "free stock audio": "zapsplat.com",
    "free book downloads": "projectgutenberg.org",
    "free online diagram tool": "draw.io",
    "css grid generator": "cssgrid-generator.netlify.app",
    "html color codes": "htmlcolorcodes.com",
    "free svg editor": "vectr.com",
    "web accessibility checker": "wave.webaim.org",
    "free icon fonts": "ionicons.com",
    "javascript debugger online": "jsdebugger.io",
    "learn react": "reactjs.org/tutorial/tutorial.html",
    "python documentation": "docs.python.org/3",
    "free hosting for static sites": "netlify.com",
    "free online database": "airtable.com",
    "interactive coding challenges": "leetcode.com",
    "free ssl certificate generator": "zerossl.com",
    "free responsive templates": "html5up.net",
    "webfont generator": "transfonter.org",
    "best css animation library": "animate.style",
    "json validator": "jsonlint.com",
    "seo keyword tool": "keywordtool.io",
    "email validation tool": "mailtester.com",
    "online regex tester": "regex101.com",
    "free website analytics": "matomo.org",
    "free ai video editor": "runwayml.com",
    "learn data visualization": "observablehq.com",
    "best online pdf to word": "smallpdf.com/pdf-to-word",
    "free code formatter": "prettier.io",
    "free ai transcription": "otter.ai",
    "online hex to rgb converter": "rgbtohex.net",
    "free blog templates": "ghost.org/themes",
    "free open data": "opendata.europa.eu",
    "free domain checker": "who.is",
    "javascript framework": "vuejs.org",
    "learning podcasts": "syntax.fm",
    "markdown viewer": "dillinger.io",
    "linux tutorial": "linuxjourney.com",
    "cybersecurity learning": "cybrary.it",
    "tech news": "techcrunch.com",
    "code pair programming": "codeshare.io",
    "font pairings": "fontpair.co",
    "ai writing ideas": "shortlyai.com",
    "css framework": "bulma.io",
    "material ui": "material-ui.com",
    "sql tutorial": "sqltutorial.org",
    "diagramming tool": "lucidchart.com",
    "kotlin docs": "kotlinlang.org/docs/home.html",
    "adobe alternatives": "krita.org",
    "svg optimizer": "svgo.io",
    "mockup generator": "placeit.net",
    "database hosting": "supabase.com",
    "online photoshop": "photopea.com",
    "cloud ide": "codeanywhere.com",
    "coding youtube channel": "thecodingtrain",
    "api docs generator": "swagger.io",
    "css inspiration": "css-tricks.com",
    "ai chatbots directory": "botlist.co",
    "javascript playground": "jsfiddle.net",
    "node.js editor": "stackblitz.com",
    "ui inspiration": "dribbble.com",
    "icon search engine": "iconfinder.com",
    "screen recording": "loom.com",
    "javascript tutorials": "javascript.info",
    "app prototyping": "invisionapp.com",
    "frontend news": "frontendfocus.co",
    "css grids": "cssgridgarden.com",
    "vector graphics software": "inkscape.org",
    "code snippet manager": "carbon.now.sh",
    "collaborative coding": "codesandbox.io",
    "data structures": "geeksforgeeks.org",
    "cloud hosting": "heroku.com",
    "python tutorials": "realpython.com",
    "css code generator": "cssportal.com",
    "color picker": "color.adobe.com",
    "email templates": "beehiiv.com/templates",
    "ai learning platform": "fast.ai",
    "web performance tools": "webpagetest.org",
    "documentation generator": "docusaurus.io",
    "javascript course": "javascript30.com",
    "api docs viewer": "redoc.ly",
    "machine learning courses": "coursera.org",
    "remote desktop": "anydesk.com",
    "css gradient generator": "cssgradient.io",
    "python playground": "trinket.io",
    "api testing online": "hoppscotch.io",
    "spreadsheet": "airtable.com",
    "html tutorials": "w3schools.com/html",
    "tech tutorials": "tutorialspoint.com",
    "real-time chat api": "pusher.com",
    "ui design tool": "penpot.app",
    "svg icon sets": "feathericons.com",
    "crm": "suitecrm.com",
    "mind map": "coggle.it",
    "css guides": "css-tricks.com/guides",
    "email newsletter builder": "mailerlite.com",
    "vector icon library": "fontello.com",
    "color blindness simulator": "colororacle.org",
    "frontend frameworks": "frontendmasters.com",
    "react learning": "scrimba.com",
    "git tutorial": "learngitbranching.js.org",
    "json editor": "jsoneditoronline.org",
    "email templates": "mjml.io",
    "prototyping tool": "figma.com/prototyping",
    "node.js learning": "nodeschool.io",
    "programming challenges": "codewars.com",
    "docker playground": "play-with-docker.com",
    "svg icon generator": "icomoon.io",
    "chatbot builder": "rasa.com",
    "flexbox generator": "the-echoplex.net/flexyboxes",
    "terminal in browser": "webshell.dev",
    "image upscaler": "letsenhance.io",
    "ux design tutorials": "uxdesign.cc",
    "privacy search": "duckduckgo.com",
    "online xml formatter": "xmlformatter.net",
    "sql tutorials": "mode.com/sql-tutorial",
    "angular docs": "angular.io",
    "js libraries": "cdnjs.com",
    "svg editor": "boxy-svg.com",
    "web scraping tutorials": "scrapinghub.com",
    "regex generator": "regexr.com",
    "linux tutorials": "linuxcommand.org",
    "security news": "thehackernews.com",
    "coding interview prep": "interviewcake.com",
    "web design templates": "templated.co",
    "cross browser testing": "browserstack.com",
    "coding bootcamps": "theodinproject.com",
    "typescript docs": "typescriptlang.org",
    "devops tutorials": "devops.com",
    "cloud storage providers": "mega.nz",
    "continuous integration": "circleci.com",
    "mobile app templates": "codecanyon.net",
    "git learning": "git-scm.com/book",
    "uml tool": "plantuml.com",
    "vector editor": "method.ac",
    "python data science": "datacamp.com",
    "javascript book": "eloquentjavascript.net",
    "sql editor": "sqlfiddle.com",
    "sass docs": "sass-lang.com",
    "image generator": "stablehorde.net",
    "ui kits": "ui8.net",
    "css reset": "meyerweb.com/eric/tools/css/reset",
    "ruby docs": "ruby-lang.org/en/documentation",
    "site speed test": "pagespeed.web.dev",
    "text diff checker": "diffchecker.com",
    "image compression": "compressjpeg.com",
    "git gui": "gitpod.io",
    "flutter docs": "flutter.dev",
    "react components": "chakra-ui.com",
    "cloud computing learning": "aws.training",
    "ecommerce platform": "magento.com",
    "css validator": "jigsaw.w3.org/css-validator",
    "html5 game tutorials": "phaser.io",
    "vector illustration packs": "undraw.co",
    "accessibility testing": "axe.dev",
    "color palettes": "colorhunt.co",
    "cybersecurity training": "hackthebox.eu",
    "analytics": "matomo.org",
    "code formatter": "beautifier.io",
    "devops learning": "kubernetes.io",
    "spreadsheet editor": "onlyoffice.com",
    "programming podcasts": "softwareengineeringdaily.com",
    "responsive templates": "bootstrapmade.com",
    "databases guide": "database.guide",
    "regex tester": "regexr.com",
    "coding contests": "topcoder.com",
    "php manual": "php.net/manual/en",
    "html css playground": "codepen.io",
    "open source fonts": "fontlibrary.org",
    "javascript console": "jsconsole.com",
    "code assistant": "tabnine.com",
    "ai education": "ai.google/education",
    "deep learning courses": "deeplearning.ai",
    "ui inspiration": "awwwards.com",
    "doc collaboration": "google.com/docs",
    "password generator": "passwordsgenerator.net",
    "cloud native learning": "cncf.io",
    "video hosting": "youtube.com",
    "audio editor": "audacityteam.org",
    "bash scripting tutorial": "linuxconfig.org/bash-scripting-tutorial",
    "static site generators": "jekyllrb.com",
    "ethics in ai": "partnershiponai.org",
    "quantum computing learning": "quantum.country",
    "data visualization tools": "tableau.com",
    "css grid learning": "cssgrid.io",
    "design systems": "designsystemsrepo.com",
    "product management": "mindtheproduct.com",
    "code sharing": "codeshare.io",
    "short entertaiming videos":"tiktok.com"
}


questions = list(faqs.keys())
vectorizer = TfidfVectorizer().fit(questions)

faq_vectors = vectorizer.transform(questions)

def chatbot():
    print("Welcome to the website finder.")
    while True:
        inp = input("you: ")
        if inp.lower() in ['stop', 'exit', 'quit']:
            print("Thank you for your time, bye!")
            break
        
        inp_vec = vectorizer.transform([inp])
        
        sim = cosine_similarity(inp_vec, faq_vectors)
        
        max_sim_idx = np.argmax(sim)
        max_sim_score = sim[0, max_sim_idx]
        
        if max_sim_score > 0.3:
            antwoord = faqs[questions[max_sim_idx]]
            print("https://", antwoord)
        else:
            print("Sorry, I do not understeand that yet.")

if __name__ == "__main__":
    chatbot()
