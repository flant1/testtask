import http.server,json,urllib.parse,re,git
class serverclass(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path.find("helloworld")==1:
			u=urllib.parse.urlparse(self.path)
			if u[4]!="":
				params=u[4].split("=")
				if params[0]!="name":
					self.send_response(200)
					self.end_headers()
					self.wfile.write(bytes("<html>wrong param</html>","utf-8"))
				else:
					name=re.findall('[A-Z][^A-Z]*',params[1])
					self.send_response(200)
					self.end_headers()
					self.wfile.write(bytes("<html>hello ","utf-8"))
					i=0
					while i<len(name):
						self.wfile.write(bytes(name[i],"utf-8"))
						self.wfile.write(bytes(" ","utf-8"))
						i+=1
					self.wfile.write(bytes("</html>","utf-8"))
			else:
				self.send_response(200)
				self.end_headers()
				self.wfile.write(bytes("<html>hello stranger</html>","utf-8"))
		elif self.path=="/versionz":
				repo=git.Repo(search_parent_directories=True)
				sha=repo.head.commit
				reponame=str(repo).split("'")
				verslist=[str(sha),reponame[1]]
				self.send_response(200)
				self.end_headers()
				self.wfile.write(bytes("<html>","utf-8"))
				self.wfile.write(bytes(str(json.dumps(verslist)),"utf-8"))
				self.wfile.write(bytes("</html>","utf-8"))
		else:
				self.send_response(200)
				self.end_headers()
				self.wfile.write(bytes("<html>wrong url</html>","utf-8"))
serverrun=http.server.HTTPServer(('192.168.56.114',8080),serverclass)
try:serverrun.serve_forever()
except:KeyboardInterrupt
