from datetime import datetime
import requests
import json


class LHM_Parser:

  def __init__(self, port=8085, ip='127.0.0.1'):

    self.port = port
    self.ip = ip

    self.raw_data = {}
    self.ram_tree = {}
    self.cpu_tree = {}
    self.gpu_tree = {}

    self.update()

  def download_data(self, port=8085, ip='127.0.0.1'):
    """
    Download the data from the LHM server.
    """
    url = f'http://{self.ip}:{self.port}/data.json'
    date_measure = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    try:
      response = requests.get(url)
      response.raise_for_status()

      return (response._content, date_measure)

    except requests.exceptions.HTTPError as err:
      print(err)
      return (None, date_measure)

  def update(self):
    """
    Update the data from the LHM server.
    """

    data, timestamp = self.download_data()
    self.raw_data_json = data
    self.raw_data_dict = json.loads(data)

    self.update_cpu_tree()
    self.update_gpu_tree()
    self.update_ram_tree()

  def export_as_dict(self):
    """
    Export the data as a dictionary.
    """
    return self.raw_data_dict

  def system_name(self):
    return self.raw_data_dict['Children'][0]['Text']

  def update_cpu_tree(self):
    """
    Update the CPU tree.
    """
    for component in self.raw_data_dict['Children'][0]['Children']:
      if component['ImageURL'] == 'images_icon/cpu.png':
        self.cpu_tree.clear()
        self.cpu_tree = component

  def update_gpu_tree(self):
    """
    Update the GPU tree.
    """
    for component in self.raw_data_dict['Children'][0]['Children']:
      if component['ImageURL'] == 'images_icon/gpu.png':
        self.gpu_tree.clear()
        self.gpu_tree = component

  def update_ram_tree(self):
    """
    Update the RAM tree.
    """
    for component in self.raw_data_dict['Children'][0]['Children']:
      if component['ImageURL'] == 'images_icon/ram.png':
        self.ram_tree.clear()
        self.ram_tree = component

# CPU FUNCTIONS ========================================================================================================

  def cpu_name(self):
    return self.cpu_tree['Text']

  def cpu_voltage_tree(self):
    for component in self.cpu_tree['Children']:
      if component['Text'] == 'Voltages':
        return component

  def cpu_power_tree(self):
    for component in self.cpu_tree['Children']:
      if component['Text'] == 'Powers':
        return component

  def cpu_clock_tree(self):
    for component in self.cpu_tree['Children']:
      if component['Text'] == 'Clocks':
        return component

  def cpu_temperature_tree(self):
    for component in self.cpu_tree['Children']:
      if component['Text'] == 'Temperatures':
        return component

  def cpu_load_tree(self):
    for component in self.cpu_tree['Children']:
      if component['Text'] == 'Load':
        return component

  def cpu_factor_tree(self):
    for component in self.cpu_tree['Children']:
      if component['Text'] == 'Factors':
        return component

# GPU FUNCTIONS ========================================================================================================

  def gpu_name(self):
    return self.gpu_tree['Text']

  def gpu_power_tree(self):
    for component in self.gpu_tree['Children']:
      if component['Text'] == 'Powers':
        return component

  def gpu_clock_tree(self):
    for component in self.gpu_tree['Children']:
      if component['Text'] == 'Clocks':
        return component

  def gpu_temperature_tree(self):
    for component in self.gpu_tree['Children']:
      if component['Text'] == 'Temperatures':
        return component

  def gpu_load_tree(self):
    for component in self.gpu_tree['Children']:
      if component['Text'] == 'Load':
        return component

  def gpu_fan_tree(self):
    for component in self.gpu_tree['Children']:
      if component['Text'] == 'Fans':
        return component

  def gpu_controls_tree(self):
    for component in self.gpu_tree['Children']:
      if component['Text'] == 'Controls':
        return component

  def gpu_data_tree(self):
    for component in self.gpu_tree['Children']:
      if component['Text'] == 'Data':
        return component

  def gpu_throughput_tree(self):
    for component in self.gpu_tree['Children']:
      if component['Text'] == 'Throughput':
        return component

# RAM FUNCTIONS ========================================================================================================

  def ram_name(self):
    return self.ram_tree['Text']

  def ram_load_tree(self):
    for component in self.ram_tree['Children']:
      if component['Text'] == 'Load':
        return component

  def ram_data_tree(self):
    for component in self.ram_tree['Children']:
      if component['Text'] == 'Data':
        return component


# DEBUG FUNCTIONS ======================================================================================================

  # def print_cpu_tree(self):
  #   print(self.cpu_tree)

  # def print_gpu_tree(self):
  #   print(self.gpu_tree)

  # def print_ram_tree(self):
  #   print(self.ram_tree)

  # def print_cpu_voltage_tree(self):
  #   for component in self.cpu_tree['Children']:
  #     if component['Text'] == 'Voltages':
  #       print(component)

  # def print_cpu_power_tree(self):
  #   for component in self.cpu_tree['Children']:
  #     if component['Text'] == 'Powers':
  #       print(component)

  # def print_cpu_clock_tree(self):
  #   for component in self.cpu_tree['Children']:
  #     if component['Text'] == 'Clocks':
  #       print(component)

  # def print_cpu_temperature_tree(self):
  #   for component in self.cpu_tree['Children']:
  #     if component['Text'] == 'Temperatures':
  #       print(component)

  # def print_cpu_load_tree(self):
  #   for component in self.cpu_tree['Children']:
  #     if component['Text'] == 'Load':
  #       print(component)

  # def print_cpu_factor_tree(self):
  #   for component in self.cpu_tree['Children']:
  #     if component['Text'] == 'Factors':
  #       print(component)
