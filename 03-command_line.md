# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > * ```pwd``` show current working directory path.
> > * ```mkdir``` create a directory.
> > * ```rm -r name_of directory``` delete a folder and all of its contents.
> > * ```touch filename.txt``` creates an empty file with the name "filename.txt".
> > * ```rm filename``` delete a file.
> > * ```mv oldfile.txt newfile.txt``` renames "oldfile" as "newfile".
> > * ```ls -a``` list all files, including hidden files.
> > * ```ls -ld .?*``` list _only_ hidden files.
> > * ```cp file.txt newdir/``` make a copy of file.txt in "newdir/".
> > * ```cat file``` view the contents of file.
> > * ```cat file1.txt > file2.txt``` take the standard output of the command on the left, and redirects it to the file2.txt. This command overwrites file2.txt if it previously existed. 
> > * ```cat file1.txt >> file2.txt``` take the standard output of the command on the left, and append it to the file2.txt.
> > * ```cat file.txt | sort ``` take the output from the command on the left and "pipes" it as the standard input to the command on the right. "Sort" orders each line alphabetically.
> > * ```grep -i "string" file.txt``` finds all lines in file.txt that has "string".
> > * ```sed 's/oldstring/newstring' file.txt``` replaces all instances of "oldstring" with "newstring" in file.txt
---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > * `ls` list files in directory.
> > * `ls -a` list _all_ files in directory including hidden files that start with "."
> > * `ls -l` list files in directory in long format.
> > * `ls -lh` list files in directory in long format with human readable file sizes.
> > * `ls -lah` list _all_ file in directory in long format, including hidden files. Print file size in human readable format. 
> > * `ls -t`  list all files in chronological order with newest at the top.
> > * `ls -Glp`  list all files in long format. Enable colorized output. Put a "/" after directories.

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > * `ls -ltr` list files in long format. Files are listed chronologically with the oldest file on the top.
> > * `ls -A` list _all_ files, including hidden files, _except_ for "." ands "..".
> > * `ls -R` list files from directory, and all subdirectories.
> > * `ls -S` list files sorted by size with the largest file at the top.
> > * `ls -U` list file using time of file creation, instead of last modification.

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` takes a standard input list, that has been piped to it, and applies a function to each item in the list. This function enables a user to replace looping bash script with a "one liner". This function is conceptually similar to python list comprehension. 
> >
> > __Example__
> > `xargs` can be used in combination with the `find` command in order to recieve a list of files meeting a criteria (such as the .py ending), and perform and operation on those files (such as deleting them).
> >
> > `find . -name "*.py" | xargs rm -rf`

 

