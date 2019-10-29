# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:22:11 2019

@author: Boyne
"""

import torch
import time as tm
import datetime as dt
from sys import stdout


class Logger(dict):

    def __init__(self, default_dict, header='', log_dir='.', file_name=''):
        '''
        A subclass of dict this adds methods to create a log file and append
        the current dictionary state to it and reset the dict to some
        defualt state.

        Parameters
        ----------

        log_dict : dictionary
            Items to save at each iteration, keys should remain constant,
            the initial values passed in should be of the type wanted to save.

        header : string
            header to put at the top of the file, must end with a \n and every
            line must begin with a #

        log_dir : string
            where to create the log file, defaults to current directory

        file_name : string
            what to save the file as, defaults to log_{current date time}.csv
        '''

        # initalise the dict
        super(Logger, self).__init__(**default_dict)

        # store the initial keys and values seperately
        self.default_keys = list(self.keys())
        self.default_values = list(self.values())

        # create the log file
        self.log_file = file_name if file_name \
            else f'log_{dt.datetime.now().strftime("%b_%d_%H-%M")}.csv'
        self._path = log_dir + '/' + self.log_file

        # create the save file
        self._create_log_file(header)

    def _csv_str(self, v):
        'fucntion to change values to a csv element safe string'
        return str(v).replace(',', ' ').replace('\n', '    ') + ','

    def _create_log_file(self, header):

        types = '# ' + ''.join([self._csv_str(v.__class__.__name__)
                                for v in self.default_values])
        columns = ''.join([self._csv_str(k) for k in self.default_keys])

        with open(self._path, 'w') as f:
            f.write(self._csv_str(header) + ','*(len(self.default_keys)-2) +
                    '\n' + types[:-1] + '\n' + columns[:-1] + '\n')

    def reset(self):

        for k, v in zip(self.default_keys, self.default_values):
            self[k] = v

    def save(self, reset_dict=True):
        'Save the current log values into the csv file'
        string = ''.join([self._csv_str(self[k]) for k in self.default_keys])
        with open(self._path, 'a') as f:
            f.write(string[:-1] + '\n')

        if reset_dict:
            self.reset()


class iteration_output():

    def __init__(self, max_iteration, prefix=''):

        self.max_iteration = max_iteration
        self.prefix = prefix
        self.start_time = None
        self.iteration = 0

        # settings
        self._time_format = lambda secs: str(dt.timedelta(seconds=int(secs)))

        # settings note implemented
        # self.output_to_file = False
        # self.sys_output = True

    def set(self, **kwargs):
        for kwarg in kwargs.keys():
            if 'prefix' in kwargs:
                self.prefix = kwargs['prefix']

            elif 'restart_time' in kwargs:
                print('Starting again at ' +
                      dt.datetime.now().strftime("%b_%d_%H-%M") + '\n')
                self.start_time = tm.time()

            elif 'iteration' in kwargs:
                self.iteration = kwargs['iteration']
                self._end_print()

            else:
                raise KeyError

    def _end_print(self):
        'print this text at the end of every epoch'

        if self.iteration >= 1:
            # print time since start
            t_pass = tm.time() - self.start_time
            string = 'runtime: ' + self._time_format(t_pass)

            etf = self.max_iteration * t_pass / (self.iteration + 1)
            string += '\t eta: ' + self._time_format(etf)

            # output
            stdout.write(f'\ri:{self.iteration}  {"finished":15}  {string:30}')
            print('')  # forces new line

    def __call__(self, string, **kwargs):

        # set the time if this is the first call
        if self.start_time is None:
            print(f'Starting at {dt.datetime.now().strftime("%b_%d_%H-%M")}\n')
            self.start_time = tm.time()

        # update the _state with any kwargs given
        if len(kwargs):
            self.set(**kwargs)

        # output
        stdout.write(f'\ri:{self.iteration}  {self.prefix:15}  {string:30}')


if __name__ == '__main__':
    log_dict = {'iteration': 0, 'var1': '', 'var2': ()}
    log = Logger(log_dict, header='# this is a test\n')
    output = iteration_output(10, prefix='first half')

    for i in range(10):

        # some dummy data
        log['iteration'] = i
        log['var1'] = 'example string'
        log['var2'] = i // 3

        # some dummy process
        output('start', iteration=i)
        tm.sleep(1)
        output('middle')
        tm.sleep(1)
        output('end')
        tm.sleep(0.1)

        # change prefix example
        if i == 5:
            output('half way', prefix='second half')

        log.save()
