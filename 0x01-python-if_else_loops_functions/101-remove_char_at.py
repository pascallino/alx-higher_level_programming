def remove_char_at(string, n):
        if n < 0 or n >= len(string):
                    return string  # No character to remove, return the original string
                    
                    char_list = list(string)
                        del char_list[n]
                            new_string = "".join(char_list)
                                
                                    return new_string

