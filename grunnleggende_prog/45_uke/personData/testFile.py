import reading_file as p_reader
import json

readingData = p_reader.read_persons("persons.csv", True)

createDict = [dict(zip(readingData[0], person)) for person in readingData[1:]]

print(type(createDict))

convertToJson = json.dumps(createDict, ensure_ascii=False)
print(type(convertToJson))
print(convertToJson)