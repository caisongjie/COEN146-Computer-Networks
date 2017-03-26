#### Lab 2: Requirements
In lab 2, the submission is in the form of a report.
Requirements are as follows:

* Table containing collected data (and an "average" column).
* Graph showing time verses size (or other way around).
* A calculation of the network bandwidth.
* Describe how the network bandwidth was calculated.
* Describe how the time was calculated.
* Describe how the data was collected.
    * If you used my script, describe in a high level what it is doing.
    * If you used your own script, you must include decent comments.
        * Also, you cannot touch the filesystem.
    * If you did everything manually, describe what you did.
        * Again, you must not touch the filesystem.
* Report in PDF (table and graph can be separate images if you want).

Wednesday Only: If your method of collecting data involves touching the
filesystem and was done before Friday 2017-01-20 UTC-8, then you can use that
data. Otherwise, you must use one of the above methods to collect data and not
touch the filesystem.


#### Lab 2: Script File
Included at the bottom of the page is a script file that will
help you collect data. Download the script file, then replace
`username` with your own.

Before using the script, you should generate ssh keys.
This is optional. However, if you do not do this, you will
need to enter your password many many times.

To generate ssh keys, do:

    mkdir -p ~/.ssh  
    ssh-keygen -t rsa -b 4096 -N '' -f ~/.ssh/id_rsa  
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys  


Before running the script, type the following command:

    chmod 0700 <the_script>


To run the script, type the following:

    ./<the_script> 2>&1 | tee <log_file>

Replace `<log_file>` with a file name.
This will save the output for future reference.
Using the data in `<log_file>`, you will write your report.

If you do not want to have a log file, simply typing `./<the_script>`
is also okay. However, the output will not be saved.



