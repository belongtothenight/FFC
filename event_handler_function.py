import converter_functions as cf
import PySimpleGUI as sg
import os
import webbrowser as wb

class Event_Handler_Function:
    def __init__(self, cl_single_conversion, cl_bulk_to_bulk_conversion, cl_file_merge, hl, window, event, values):
        self.cl_single_conversion = cl_single_conversion
        self.cl_bulk_to_bulk_conversion = cl_bulk_to_bulk_conversion
        self.cl_file_merge = cl_file_merge
        self.hl = hl
        self.window = window
        self.event = event
        self.values = values
        
    #==================================================================================================================
    # Menu Bar

    def execution_log_update(self):
        print('============ Event = ', self.event, ' ==============')
        print('-------- Values Dictionary (key=value) --------')
        for key in self.values:
            print(key, ' = ',self.values[key])

    def menu_event(self):
        print("[LOG] cl_single_conversionicked " + self.event + "!")
        if self.event == self.cl_single_conversion[0]:
            sg.popup(
                "This function converts md file (table)  to csv files in the same folder. It can only convert the first table in markdown file correctly.",
                keep_on_top=True,
                title=self.cl_single_conversion[0] + ' Description'
                )
        elif self.event == self.cl_single_conversion[1]:
            sg.popup(
                "This function converts single csv file to md file (table) .",
                keep_on_top=True,
                title=self.cl_single_conversion[1] + ' Description'
                )
        elif self.event == self.cl_single_conversion[2]:
            sg.popup(
                "This function converts single xml file exported from labelimg to csv file.",
                keep_on_top=True,
                title=self.cl_single_conversion[2] + ' Description'
                )
        elif self.event == self.cl_single_conversion[3]:
            sg.popup(
                "This function converts single csv file to parquet file.",
                keep_on_top=True,
                title=self.cl_single_conversion[3] + ' Description'
                )
        elif self.event == self.cl_single_conversion[4]:
            sg.popup(
                "This function converts single parquet file to csv file.",
                keep_on_top=True,
                title=self.cl_single_conversion[4] + ' Description'
                )
        elif self.event == self.cl_single_conversion[5]:
            sg.popup(
                "This function renames the single file specified.",
                keep_on_top=True,
                title=self.cl_single_conversion[5] + ' Description'
                )
        elif self.event == self.cl_bulk_to_bulk_conversion[0]:
            sg.popup(
                "This function convert md files (table)  to csv files.",
                keep_on_top=True,
                title=self.cl_bulk_to_bulk_conversion[0] + ' Description'
                )
        elif self.event == self.cl_bulk_to_bulk_conversion[1]:
            sg.popup(
                "This function convert csv files to md files (table) .",
                keep_on_top=True,
                title=self.cl_bulk_to_bulk_conversion[1] + ' Description'
                )
        elif self.event == self.cl_bulk_to_bulk_conversion[2]:
            sg.popup(
                "This function convert xml files to csv files.",
                keep_on_top=True,
                title=self.cl_bulk_to_bulk_conversion[2] + ' Description'
                )
        elif self.event == self.cl_bulk_to_bulk_conversion[3]:
            sg.popup(
                "This function convert csv files to parquet files.",
                keep_on_top=True,
                title=self.cl_bulk_to_bulk_conversion[3] + ' Description'
                )
        elif self.event == self.cl_bulk_to_bulk_conversion[4]:
            sg.popup(
                "This function convert parquet files to csv files.",
                keep_on_top=True,
                title=self.cl_bulk_to_bulk_conversion[4] + ' Description'
                )
        elif self.event == self.cl_bulk_to_bulk_conversion[5]:
            sg.popup(
                "This function rename all the specified type of files.",
                keep_on_top=True,
                title=self.cl_bulk_to_bulk_conversion[5] + ' Description'
                )
        elif self.event == self.cl_file_merge[0]:
            sg.popup(
                "This function merges multiple csv files into one csv file.",
                keep_on_top=True,
                title=self.cl_file_merge[0] + ' Description'
                )
        elif self.event == self.cl_file_merge[1]:
            sg.popup(
                "This function merges multiple parquet files into one parquet file.",
                keep_on_top=True,
                title=self.cl_file_merge[1] + ' Description'
                )
        elif self.event == self.cl_file_merge[2]:
            sg.popup(
                "This function merges multiple md files (table) into one md file.",
                keep_on_top=True,
                title=self.cl_file_merge[2] + ' Description'
                )
        elif self.event == self.cl_file_merge[3]:
            sg.popup(
                "This function merges multiple xml files into one csv file.",
                keep_on_top=True,
                title=self.cl_file_merge[3] + ' Description'
                )
        elif self.event == self.hl[0]:
            print("[LOG] Clicked " + self.hl[0] + " !")
            wb.open('https://github.com/belongtothenight/File-Format-Converter')
        elif self.event == self.hl[1]:
            print("[LOG] Clicked " + self.hl[1] + " !")
            wb.open('https://github.com/belongtothenight/File-Format-Converter/issues')
        elif self.event == self.hl[2]:
            print("[LOG] Clicked " + self.hl[2] + " !")
            wb.open('https://github.com/belongtothenight/File-Format-Converter/discussions')
            

    #==================================================================================================================
    # Single Conversion

    def listbox_update(self, listbox, folder, flag):
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        fname = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            #and f.lower().endswith(('.md', '.csv', '.xml', '.parquet')) # add file format filter
        ]
        self.window[listbox].update(fname)
        if flag == 'source':
            self.window['-R1-'].update(value=True)
            self.window['-R2-'].update(value=False)
        elif flag == 'export':
            self.window['-R1-'].update(value=False)
            self.window['-R2-'].update(value=True)
        else:
            pass
        return fname

    def conversion_source_folder(self):
        source_folder = self.values[self.event]
        print('[LOG] Source Folder = ', source_folder)
        source_folder_list = self.listbox_update("-LISTBOX-", source_folder, 'source')
        return source_folder, source_folder_list

    def conversion_source_filename(self):
        source_filename = self.values[self.event]
        print('[LOG] Source Filename = ', source_filename)
        return source_filename

    def conversion_export_folder(self):
        export_folder = self.values[self.event]
        print('[LOG] Export Folder = ', export_folder)
        export_folder_list = self.listbox_update("-LISTBOX-", export_folder, 'export')
        return export_folder, export_folder_list

    def conversion_export_filename(self):
        export_filename = self.values[self.event]
        print('[LOG] Export Filename = ', export_filename)
        return export_filename

    def single_conversion_filename_varification(self, converter, source_filename, export_filename, source_folder_list):
        if converter == self.cl_single_conversion[0] and source_filename.endswith(('.md'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) : # filename typed, source file exists
            converter_check = 'Converter Selected: ' + converter + ' => Valid!'
            print("[LOG] " + converter_check)
            self.window['-OUTPUT-'].update(converter_check, text_color='green')
        elif converter == self.cl_single_conversion[0] and source_filename.endswith(('.md'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) == False: # filename typed, source file error
            converter_check = 'Source file doesn\'t exist!'
            print("[LOG] Source file doesn\'t exist!")
            self.window['-OUTPUT-'].update(converter_check, text_color='red')
        elif converter == self.cl_single_conversion[1] and source_filename.endswith(('.csv'))  and export_filename.endswith(('.md'))  and (source_filename in source_folder_list) : # filename typed, source file exists
            converter_check = 'Converter Selected: ' + converter + ' => Valid!'
            print("[LOG] " + converter_check)
            self.window['-OUTPUT-'].update(converter_check, text_color='green')
        elif converter == self.cl_single_conversion[1] and source_filename.endswith(('.csv'))  and export_filename.endswith(('.md'))  and (source_filename in source_folder_list) == False: # filename typed, source file error
            converter_check = 'Source file doesn\'t exist!'
            print("[LOG] Source file doesn\'t exist!")
            self.window['-OUTPUT-'].update(converter_check, text_color='red')
        elif converter == self.cl_single_conversion[2] and source_filename.endswith(('.xml'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) : # filename typed, source file exists
            converter_check = 'Converter Selected: ' + converter + ' => Valid!'
            print("[LOG] " + converter_check)
            self.window['-OUTPUT-'].update(converter_check, text_color='green')
        elif converter == self.cl_single_conversion[2] and source_filename.endswith(('.xml'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) == False: # filename typed, source file error
            converter_check = 'Source file doesn\'t exist!'
            print("[LOG] Source file doesn\'t exist!")
            self.window['-OUTPUT-'].update(converter_check, text_color='red')
        elif converter == self.cl_single_conversion[3] and source_filename.endswith(('.csv'))  and export_filename.endswith(('.parquet'))  and (source_filename in source_folder_list) : # filename typed, source file exists
            converter_check = 'Converter Selected: ' + converter + ' => Valid!'
            print("[LOG] " + converter_check)
            self.window['-OUTPUT-'].update(converter_check, text_color='green')
        elif converter == self.cl_single_conversion[3] and source_filename.endswith(('.csv'))  and export_filename.endswith(('.parquet'))  and (source_filename in source_folder_list) == False: # filename typed, source file error
            converter_check = 'Source file doesn\'t exist!'
            print("[LOG] Source file doesn\'t exist!")
            self.window['-OUTPUT-'].update(converter_check, text_color='red')
        elif converter == self.cl_single_conversion[4] and source_filename.endswith(('.parquet'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) : # filename typed, source file exists
            converter_check = 'Converter Selected: ' + converter + ' => Valid!'
            print("[LOG] " + converter_check)
            self.window['-OUTPUT-'].update(converter_check, text_color='green')
        elif converter == self.cl_single_conversion[4] and source_filename.endswith(('.parquet'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) == False: # filename typed, source file error
            converter_check = 'Source file doesn\'t exist!'
            print("[LOG] Source file doesn\'t exist!")
            self.window['-OUTPUT-'].update(converter_check, text_color='red')
        elif converter == self.cl_single_conversion[5]  and (source_filename in source_folder_list) :
            converter_check = 'Converter Selected: ' + converter + ' => Valid!'
            print("[LOG] " + converter_check)
            self.window['-OUTPUT-'].update(converter_check, text_color='green')
        elif converter == self.cl_single_conversion[5] and (source_filename in source_folder_list) == False:
            converter_check = 'Source file doesn\'t exist!'
            print("[LOG] Source file doesn\'t exist!")
            self.window['-OUTPUT-'].update(converter_check, text_color='red')
        else:
            converter_check = 'Converter Selected: ' + converter + ' => InValid!'
            print("[LOG] " + converter_check)
            self.window['-OUTPUT-'].update(converter_check, text_color='red')

    def single_conversion_converter(self, source_filename, export_filename, source_folder_list):
        print("[LOG] Selected Option Menu!")
        converter = self.values['-OPTION MENU-']
        print("[LOG] Converter selected: " + converter)
        converter_check = 'Converter Selected: ' + converter
        self.window['-OUTPUT-'].update(converter_check)
        try:
            self.single_conversion_filename_varification(converter, source_filename, export_filename, source_folder_list)
        except:
            converter_check = 'Please type filenames.'
            print("[LOG] " + converter_check)
            self.window['-OUTPUT-'].update(converter_check, text_color='red')
        return converter, converter_check

    def single_conversion_convert_and_export(self, converter, source_folder, export_folder, source_filename, export_filename):
        if converter == self.cl_single_conversion[0]:
            if cf.md_to_csv(source_folder, export_folder, source_filename, export_filename) :
                print("[LOG] Conversion complete, File exported!")
                self.window['-OUTPUT0-'].update('File exported!', text_color='green')
        elif converter == self.cl_single_conversion[1]:
            if cf.csv_to_md(source_folder, export_folder, source_filename, export_filename, "Test", "Test") : # h1 and frame doesn't work here
                print("[LOG] Conversion complete, File exported!")
                self.window['-OUTPUT0-'].update('File exported!', text_color='green')
        elif converter == self.cl_single_conversion[2]:
            if cf.xml_to_csv(source_folder, export_folder, source_filename, export_filename) :
                print("[LOG] Conversion complete, File exported!")
                self.window['-OUTPUT0-'].update('File exported!', text_color='green')
        elif converter == self.cl_single_conversion[3]:
            if cf.csv_to_parquet(source_folder, export_folder, source_filename, export_filename) :
                print("[LOG] Conversion complete, File exported!")
                self.window['-OUTPUT0-'].update('File exported!', text_color='green')
        elif converter == self.cl_single_conversion[4]:
            if cf.parquet_to_csv(source_folder, export_folder, source_filename, export_filename) :
                print("[LOG] Conversion complete, File exported!")
                self.window['-OUTPUT0-'].update('File exported!', text_color='green')
        elif converter == self.cl_single_conversion[5]:
            if cf.file_rename(source_folder, export_folder, source_filename, export_filename) :
                print("[LOG] Conversion complete, File exported!")
                self.window['-OUTPUT0-'].update('File exported!', text_color='green')
        else:
            print("[LOG] Conversion error, no file exported.")
            self.window['-OUTPUT0-'].update('Error!', text_color='red')
        export_folder_list = self.listbox_update("-LISTBOX-", export_folder, 'export')

    def single_conversion_convert_and_export_check(self, converter, converter_check, source_folder, export_folder, source_filename, export_filename):
        try:
            if converter == '':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Converter not selected.', text_color='red')
            elif converter_check == 'Please type filenames.':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
            elif converter_check == 'Converter Selected: ' + self.cl_single_conversion[0] + ' => InValid!':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
            elif converter_check == 'Converter Selected: ' + self.cl_single_conversion[1] + ' => InValid!':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
            elif converter_check == 'Converter Selected: ' + self.cl_single_conversion[2] + ' => InValid!':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
            elif converter_check == 'Converter Selected: ' + self.cl_single_conversion[3] + ' => InValid!':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
            elif converter_check == 'Converter Selected: ' + self.cl_single_conversion[4] + ' => InValid!':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
            elif converter_check == 'Converter Selected: ' + self.cl_single_conversion[5] + ' => InValid!':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
            elif converter_check == 'Source file doesn\'t exist!':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Please re-type source filename.', text_color='red')
            else:
                # run conversion and export
                self.single_conversion_convert_and_export(converter, source_folder, export_folder, source_filename, export_filename)
        except:
            print("[LOG] Converter selected: None")
            self.window['-OUTPUT0-'].update('Please select converter.', text_color='red')

    def single_conversion_view_source_folder(self, source_folder):
        print("[LOG] Selected view source folder!")
        try:
            source_folder_list = self.listbox_update(self.event, source_folder, 'source')
        except:
            source_folder = ''
            source_folder_list = self.listbox_update(self.event, source_folder, 'source')

    def single_conversion_view_export_folder(self, export_folder):
        print("[LOG] Selected view export folder!")
        try:
            export_folder_list = self.listbox_update(self.event, export_folder, 'export')
        except:
            export_folder = ''
            export_folder_list = self.listbox_update(self.event, export_folder, 'export')

    def single_conversion_file_preview(self, source_folder, export_folder):
        if self.values['-R1-'] == True and self.values['-R2-'] == False:
            folder = source_folder
        elif self.values['-R1-'] == False and self.values['-R2-'] == True:
            folder = export_folder
        try:
            with open(folder + '/' + self.values["-LISTBOX-"][0], 'r') as f:
                self.window['-ML-'+sg.WRITE_ONLY_KEY].update('')
                source_file = f.read()
                self.window['-ML-'+sg.WRITE_ONLY_KEY].print(source_file)
                f.close()
        except:
            pass

    #==================================================================================================================
    # Bulk Conversion

    def bulk_conversion_listbox_update(self, listbox, folder, flag):
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        fname = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            #and f.lower().endswith(('.md', '.csv', '.xml', '.parquet')) # add file format filter
        ]
        self.window[listbox].update(fname)
        return fname

    def bulk_conversion_source_folder(self):
        source_folder = self.values['-FOLDER-1']
        print('[LOG] Source Folder = ', source_folder)
        source_folder_list = self.bulk_conversion_listbox_update('-LISTBOX-1', source_folder, 'source')
        return source_folder, source_folder_list

    def bulk_conversion_export_folder(self):
        export_folder = self.values['-FOLDER-2']
        print('[LOG] Export Folder = ', export_folder)
        export_folder_list = self.bulk_conversion_listbox_update('-LISTBOX-2', export_folder, 'export')
        return export_folder, export_folder_list

    def bulk_conversion_select(self):
        print("[LOG] Select Bulk to Bulk Conversion => " + self.values['-OPTION MENU-0'])
        converter = self.values['-OPTION MENU-0']
        self.window['-TXT-1'].update('Selected Converter: ' + converter, text_color='green')
        if self.values['-OPTION MENU-0'] == self.cl_bulk_to_bulk_conversion[5]:
            self.window['-TXT-'].update(text_color='black')
            self.window['-TXT-0'].update(text_color='black')
            self.window['-INPUT-1'].update(disabled=False)
            self.window['-INPUT-2'].update(disabled=False)
        else:
            self.window['-TXT-'].update(text_color='grey')
            self.window['-TXT-0'].update(text_color='grey')
            self.window['-INPUT-1'].update(disabled=True)
            self.window['-INPUT-2'].update(disabled=True)
        return converter

    def bulk_conversion_convert_and_export(self, converter, source_folder, export_folder):
        print("[LOG] Select Bulk to Bulk Conversion and Export")
        self.window['-TXT-2'].update('Start Converting...', text_color='green')
        if converter == self.cl_bulk_to_bulk_conversion[0]:
            cf.bulk_md_to_csv(self.values['-FOLDER-1'], self.values['-FOLDER-2'])
        elif converter == self.cl_bulk_to_bulk_conversion[1]:
            cf.bulk_csv_to_md(self.values['-FOLDER-1'], self.values['-FOLDER-2'])
        elif converter == self.cl_bulk_to_bulk_conversion[2]:
            cf.bulk_xml_to_csv(self.values['-FOLDER-1'], self.values['-FOLDER-2'])
        elif converter == self.cl_bulk_to_bulk_conversion[3]:
            cf.bulk_csv_to_parquet(self.values['-FOLDER-1'], self.values['-FOLDER-2'])
        elif converter == self.cl_bulk_to_bulk_conversion[4]:
            cf.bulk_parquet_to_csv(self.values['-FOLDER-1'], self.values['-FOLDER-2'])
        elif converter == self.cl_bulk_to_bulk_conversion[5]:
            cf.bulk_rename(self.values['-FOLDER-1'], self.values['-FOLDER-2'], self.values['-INPUT-1'], self.values['-INPUT-2'])
        print("[LOG] " + converter + " executed!")
        source_folder_list = self.bulk_conversion_listbox_update('-LISTBOX-1', source_folder, 'source')
        export_folder_list = self.bulk_conversion_listbox_update('-LISTBOX-2', export_folder, 'export')
        return source_folder_list, export_folder_list

    #==================================================================================================================
    # File Merge

    def file_merge_listbox_update(self, listbox, folder):
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        fname = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            #and f.lower().endswith(('.md', '.csv', '.xml', '.parquet')) # add file format filter
        ]
        self.window[listbox].update(fname)
        return fname

    def file_merge_source_folder(self):
        source_folder = self.values['-FOLDER-3']
        print("[LOG] File Merge >> Source Folder: " + source_folder)
        source_folder_list = self.file_merge_listbox_update('-LISTBOX-3', source_folder)
        self.window['-R1-3'].update(value=True)
        self.window['-R2-3'].update(value=False)
        return source_folder, source_folder_list

    def file_merge_export_folder(self):
        export_folder = self.values['-FOLDER-4']
        print("[LOG] File Merge >> Export Folder: " + export_folder)
        export_folder_list = self.file_merge_listbox_update('-LISTBOX-3', export_folder)
        self.window['-R1-3'].update(value=False)
        self.window['-R2-3'].update(value=True)
        return export_folder, export_folder_list

    def file_merge_export_filename(self):
        export_filename = self.values['-INPUT-4']
        print("[LOG] File Merge >> Export Filename: " + export_filename)
        self.window['-R1-3'].update(value=False)
        self.window['-R2-3'].update(value=True)
        return export_filename

    def file_merge_select(self):
        converter = self.values['-OPTION MENU-2']
        print("[LOG] File Merge >> Converter: " + converter)
        self.window['-TXT-3'].update('Selected Converter: ' + converter, text_color='green')
        return converter

    def file_merge_convert_and_export(self, converter, source_folder, export_folder, export_filename):
        self.window['-TXT-4'].update('Start Converting...', text_color='green')
        if converter == self.cl_file_merge[0]:
            cf.merge_csv(source_folder, export_folder, export_filename)
        elif converter == self.cl_file_merge[1]:
            cf.merge_parquet(source_folder, export_folder, export_filename)
        elif converter == self.cl_file_merge[2]:
            cf.merge_md(source_folder, export_folder, export_filename)
        elif converter == self.cl_file_merge[3]:
            cf.merge_xml_to_csv(source_folder, export_folder, export_filename)
        print("[LOG] File Merge >> Exported: " + export_filename)
        export_folder_list = self.file_merge_listbox_update('-LISTBOX-3', export_folder)
        self.window['-R1-3'].update(value=False)
        self.window['-R2-3'].update(value=True)
        return export_folder_list

    def file_merge_file_preview(self, source_folder, export_folder):
        if self.values['-R1-3'] == True and self.values['-R2-3'] == False:
            folder = source_folder
        elif self.values['-R1-3'] == False and self.values['-R2-3'] == True:
            folder = export_folder
        try:
            with open(folder + '/' + self.values["-LISTBOX-3"][0], 'r') as f:
                self.window['-ML-3'+sg.WRITE_ONLY_KEY].update('')
                source_file = f.read()
                self.window['-ML-3'+sg.WRITE_ONLY_KEY].print(source_file)
                f.close()
        except:
            pass


if __name__ == '__main__':
    print("This is event handler file, not main.")