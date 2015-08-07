#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>
#include <ctype.h>
#include <pciaccess.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <getopt.h>
#include <time.h>
#include <fcntl.h>
#include <errno.h>




/*static char *log_file = NULL;*/




int main(int argc, char *argv[]) {


	log_file[] = "/var/log/gpu-manager.log";

    /* Send messages to the log or to stdout */
    if (log_file || (!log_handle = fopen(log_file, "w"))) {

        log_handle = fopen(log_file, "w");

        if (!log_handle) {
            /* Use stdout */
            log_handle = stdout;
            fprintf(log_handle, "Warning: writing to %s failed (%s)\n",
                    log_file, strerror(errno));
        }
    }
    else {
        log_handle = stdout;
    }


}